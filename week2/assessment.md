```
1. For classifying product names to categories:

    1.a. What precision (P@1) were you able to achieve?

        ~0.9

    1.b. What fastText parameters did you use?

        -epoch 25 -wordNgrams 2 -lr 1.0

        Tried auto-tune, but these hand-tuned parameters were better (and far faster).

    1.c. How did you transform the product names?

        Using CLI tools they were stripped, lowercased, etc.

    1.d. How did you prune infrequent category labels, and how did that affect your precision?

        Pruned by using `Counter()` to just the categories that had less than
        500 examples. As mentioned in the materials, you should have _at least_
        50 examples per category, but preferably more.

        Precision went way up when we had more examples for each category!

    1.e. How did you prune the category tree, and how did that affect your precision?

        This is referring to the optional task? I didn't do that one.

2. For deriving synonyms from content:

    2.a. What were the results for your best model in the tokens used for evaluation?

        Query word? iphone
            4s 0.840441
            apple 0.791758
            3gs 0.743994
            ipod 0.718704
            ipad 0.662564
            4th 0.599328
            ifrogz 0.5555
            3g 0.554638
            mophie 0.551765
            macbeth 0.545212

    2.b. What fastText parameters did you use?

        -epoch 25

    2.c. How did you transform the product names?

        Using the Unix CLI tools in the example to do some poor man stemming: lowercase, remove
        punctuation, etc.

3. For integrating synonyms with search:

    3.a. How did you transform the product names (if different than previously)?
        
        Same as before

    3.b. What threshold score did you use?
        
        0.75

    3.c. Were you able to find the additional results by matching synonyms?

        Yes! The recall went way up.

3. For classifying reviews:

    I did not complete this optional task.
```
