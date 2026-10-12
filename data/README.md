# Data

`sample_social_posts.csv` contains anonymized, paraphrased public-discussion examples for prototype validation.

The repository does not attempt to identify real users.

Recommended production workflow:
1. collect permitted public or first-party data
2. remove personal identifiers
3. label persona / topic / risk / stage
4. split train / validation / test sets
5. calibrate churn scoring against real outcomes
6. apply access control and retention policies
