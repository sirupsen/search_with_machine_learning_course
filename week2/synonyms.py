import fasttext

model = fasttext.load_model("/workspace/datasets/fasttext/title_model.bin")

with open("/workspace/datasets/fasttext/synonyms.csv", "w") as output, open(
    "/workspace/datasets/fasttext/top_words.txt", "r"
) as input:
    for word in input:
        word = word.strip()
        neighbours = model.get_nearest_neighbors(word)
        synonyms = [w.strip() for (similarity, w) in neighbours if similarity >= 0.75 and w.strip() != word]
        if len(synonyms) > 0:
            output.write(f"{word.strip()},{','.join(synonyms)}\n")
