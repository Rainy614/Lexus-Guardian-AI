from src.risk_scoring import calculate_churn_score, get_risk_level
from src.churn_journey import classify_journey_stage, detect_primary_trigger
from src.next_best_action import recommend_action

def run_demo():
    text = "最近回原廠又叫我換一堆東西，報價快三萬，有人推薦台北 Lexus 外廠嗎？"
    persona = "價格敏感型"
    risks = {
        "price_risk": 88,
        "trust_risk": 76,
        "service_risk": 55,
        "transparency_risk": 84,
        "alternative_risk": 96,
    }

    score = calculate_churn_score(**risks)
    stage = classify_journey_stage(text)

    result = {
        "input": text,
        "persona": persona,
        "churn_score": score,
        "risk_level": get_risk_level(score),
        "journey_stage": stage,
        "primary_trigger": detect_primary_trigger(text),
        "next_best_action": recommend_action(persona, stage, risks),
    }

    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    run_demo()
