from src.risk_scoring import calculate_churn_score, get_risk_level
from src.churn_journey import classify_journey_stage

def test_churn_score():
    score = calculate_churn_score(80, 80, 80, 80, 80)
    assert score == 80.0
    assert get_risk_level(score) == "High"

def test_alternative_stage():
    assert classify_journey_stage("有人推薦 Lexus 外廠嗎？") == "Stage 4 - Alternative Search"
