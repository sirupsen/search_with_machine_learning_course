## For query classification:

**How many unique categories did you see in your rolled up training data when you set the minimum number of queries per category to 1000? To 10000?**

This turned out to be much more work than I anticipated, but I may have over-compensated on correctness..? My implementation does a BFS (i.e. one layer at a time) from the leaves, walking up to the parents. If you do it the naive way described in the course, it doesn't give the correct result. Imagine a result where you have `min_queries=3` and this branch, where the number denotes the number of queries:

```
       0 = Home
       0 = Home Entertainment
2 = Console     1 = TV
```

If you just join TV upwards until it has a hit, it'll end up at Home. You need to process the entire level at a time, so you get 3 queries rolled up at Home Entertainment, to avoid escalating up to Home.

Maybe I'm missing something simpler?

min_queries 1,000:  437
min_queries 10,000: 114

**What were the best values you achieved for R@1, R@3, and R@5? You should have tried at least a few different models, varying the minimum number of queries per category, as well as trying different fastText parameters or query normalization. Report at least 2 of your runs.**

The way I understand it, recall here means for what % of queries the predicted labels is among the top @1, @2, or @3 results.

min_queries=1000, normalized, default LR, default epochs: 

R@1 of 0.482
R@3 of 0.637
R@5 of 0.701

min_queries=10000, normalized, default LR, default epochs:

R@1 of 0.574
R@3 of 0.765
R@5 of 0.821

As expected, higher `min_queries` leads to higher recall

## For integrating query classification with search:

**Give 2 or 3 examples of queries where you saw a dramatic positive change in the results because of filtering. Make sure to include the classifier output for those queries.**

Phones and earphones was less noisy

iPhone was less noisy

**Give 2 or 3 examples of queries where filtering hurt the results, either because the classifier was wrong or for some other reason. Again, include the classifier output for those queries.**

Raw model numbers easily have a strong bias, e.g. 3 mapping to same category as iPhone. 3 could mean lots of things.