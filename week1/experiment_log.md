# (1) Baseline LTR on name

Simple MRR is 0.279
LTR Simple MRR is 0.145
Hand tuned MRR is 0.423
LTR Hand Tuned MRR is 0.167

Simple p@10 is 0.120
LTR simple p@10 is 0.065
Hand tuned p@10 is 0.171
LTR hand tuned p@10 is 0.072
Simple better: 662      LTR_Simple Better: 431  Equal: 21
HT better: 713  LTR_HT Better: 564      Equal: 12

# (2) LTR w/ Name Match Phrase

Simple MRR is 0.279
LTR Simple MRR is 0.145
Hand tuned MRR is 0.423
LTR Hand Tuned MRR is 0.167

Simple p@10 is 0.120
LTR simple p@10 is 0.065
Hand tuned p@10 is 0.171
LTR hand tuned p@10 is 0.072
Simple better: 662      LTR_Simple Better: 431  Equal: 21
HT better: 713  LTR_HT Better: 564      Equal: 12

# (3) LTR w/ customer reveiew average and count

review_avg factor 2, modifier none, missing 0
customer_review_count factor 1, modifier none, missing 0

Simple MRR is 0.279
LTR Simple MRR is 0.352
Hand tuned MRR is 0.423
LTR Hand Tuned MRR is 0.336

Simple p@10 is 0.120
LTR simple p@10 is 0.144
Hand tuned p@10 is 0.171
LTR hand tuned p@10 is 0.152
Simple better: 488      LTR_Simple Better: 616  Equal: 10
HT better: 612  LTR_HT Better: 658      Equal: 19

# (4) LTR w/ HIGH customer reveiew average and count (WORSE)

review_avg factor 10, modifier none, missing 0
customer_review_count factor 10, modifier log, missing 0

Simple MRR is 0.279
LTR Simple MRR is 0.025
Hand tuned MRR is 0.423
LTR Hand Tuned MRR is 0.025

Simple p@10 is 0.120
LTR simple p@10 is 0.009
Hand tuned p@10 is 0.171
LTR hand tuned p@10 is 0.009
Simple better: 7        LTR_Simple Better: 5    Equal: 1
HT better: 6    LTR_HT Better: 6        Equal: 1

# (5) LTR add artist name, short and long description (BETTER)

Simple MRR is 0.279
LTR Simple MRR is 0.414
Hand tuned MRR is 0.423
LTR Hand Tuned MRR is 0.390

Simple p@10 is 0.120
LTR simple p@10 is 0.159
Hand tuned p@10 is 0.171
LTR hand tuned p@10 is 0.176
Simple better: 443      LTR_Simple Better: 665  Equal: 6
HT better: 538  LTR_HT Better: 742      Equal: 9

# (6) LTR with sales rank

Simple MRR is 0.279
LTR Simple MRR is 0.431
Hand tuned MRR is 0.423
LTR Hand Tuned MRR is 0.401

Simple p@10 is 0.120
LTR simple p@10 is 0.171
Hand tuned p@10 is 0.171
LTR hand tuned p@10 is 0.185
Simple better: 448      LTR_Simple Better: 660  Equal: 6
HT better: 590  LTR_HT Better: 687      Equal: 12
