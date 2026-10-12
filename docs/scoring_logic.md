# Churn Scoring Logic — v0.1

```text
Churn Score =
Price Risk × 0.20
+ Trust Risk × 0.25
+ Service Risk × 0.15
+ Transparency Risk × 0.15
+ Alternative Risk × 0.25
```

Risk levels:
- Low: score < 50
- Medium: 50 <= score < 75
- High: score >= 75

The weights are prototype assumptions, not final scientific estimates.

Validation roadmap:
1. manually labeled dataset
2. inter-rater agreement
3. compare heuristic scoring with model output
4. calibrate against real return-to-service outcomes
5. evaluate precision, recall, F1, and calibration
