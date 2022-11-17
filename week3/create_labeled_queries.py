import os
import argparse
import time
import re
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import csv

# Useful if you want to perform stemming.
import nltk
from pandas.core.window import RollingGroupby
stemmer = nltk.stem.PorterStemmer()

categories_file_name = r'/workspace/datasets/product_data/categories/categories_0001_abcat0010000_to_pcmcat99300050000.xml'

queries_file_name = r'/workspace/datasets/train.csv'
output_file_name = r'/workspace/datasets/fasttext/labeled_queries.txt'

parser = argparse.ArgumentParser(description='Process arguments.')
general = parser.add_argument_group("general")
general.add_argument("--min_queries", default=1,  help="The minimum number of queries per category label (default is 1)")
general.add_argument("--output", default=output_file_name, help="the file to output to")

args = parser.parse_args()
output_file_name = args.output

if args.min_queries:
    min_queries = int(args.min_queries)
else:
    min_queries = 1

# The root category, named Best Buy with id cat00000, doesn't have a parent.
root_category_id = 'cat00000'

tree = ET.parse(categories_file_name)
root = tree.getroot()

# Parse the category XML file to map each category id to its parent category id in a dataframe.
categories = []
parents = []
for child in root:
    id = child.find('id').text
    cat_path = child.find('path')
    cat_path_ids = [cat.find('id').text for cat in cat_path]
    leaf_id = cat_path_ids[-1]
    if leaf_id != root_category_id:
        categories.append(leaf_id)
        parents.append(cat_path_ids[-2])
parents_df = pd.DataFrame(list(zip(categories, parents)), columns =['category', 'parent'])

# Read the training data into pandas, only keeping queries with non-root categories in our category tree.
queries_df = pd.read_csv(queries_file_name)[['category', 'query']]
queries_df = queries_df[queries_df['category'].isin(categories)]


# Convert queries to lowercase, and optionally implement other normalization, like stemming.
elapsed = time.monotonic()
def normalize_query(query):
    query = query.lower()
    query = re.sub(r'[^A-Za-z0-9+]', ' ', query)  # remove non alphanumeric
    query = re.sub(r' +', ' ', query)  # remove double-spaces, e.g. from previous
    query = query.strip()
    return ' '. join([stemmer.stem(word) for word in query.split(' ')])


test_str = "Beats By Dr. Dre- Monster Pro Over-the-Ear Headphones"
expected = 'beat by dr dre monster pro over the ear headphon'
assert normalize_query(test_str) == expected
queries_df['query'] = queries_df['query'].apply(normalize_query)
print("Time to normalize queries: {:.2f} seconds".format(time.monotonic() - elapsed))

def is_leaf(row) -> bool:
    return len(parents_df[parents_df['parent'] == row.name]) == 0


elapsed = time.monotonic()
category_counts = queries_df.groupby('category').count()

parents_df = parents_df.set_index('category').join(category_counts)
parents_df = parents_df.sort_values("parent")

parents_df['query'].fillna(0.0, inplace=True)
parents_df['query'] = parents_df['query'].astype('int32')
parents_df['is_leaf'] = parents_df.apply(is_leaf, axis=1)

queries_df['rollup_category'] = queries_df['category']

leaf_nodes = parents_df[(parents_df['is_leaf'] == True) & (parents_df['query'] > 0)]
fifo = []
fifo += leaf_nodes.index.tolist()

while len(fifo) > 0:
    print(len(fifo))

    category = fifo.pop(0)
    node = parents_df.loc[category]

    if node.query >= min_queries:
        queries_df.loc[queries_df['rollup_category'] == node.name,
                       'rollup_category'] = node.name
    else:
        queries_df.loc[queries_df['rollup_category'] == node.name,
                       'rollup_category'] = node.parent
        if node.parent != 'cat00000':
            parent = parents_df.loc[node.parent]

            parent_queries = parent.query + node.query
            parents_df.loc[node.parent, 'query'] = parent_queries

            if len(fifo) == 0 or fifo[-1] != node.parent:
                fifo.append(node.parent)

# Create labels in fastText format.
queries_df['label'] = '__label__' + queries_df['rollup_category']

import pdb
pdb.set_trace()

# Output labeled query data as a space-separated file, making sure that every category is in the taxonomy.
queries_df = queries_df[queries_df['rollup_category'].isin(categories)]
queries_df['output'] = queries_df['label'] + ' ' + queries_df['query']
queries_df[['output']].to_csv(output_file_name, header=False, sep='|', escapechar='\\', quoting=csv.QUOTE_NONE, index=False)