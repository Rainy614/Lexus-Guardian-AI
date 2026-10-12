WEIGHTS = {
    "price_risk": 0.20,
    "trust_risk": 0.25,
    "service_risk": 0.15,
    "transparency_risk": 0.15,
    "alternative_risk": 0.25,
}

def _validate_score(value):
    if not 0 <= value <= 100:
        raise ValueError("Risk scores must be between 0 and 100.")

def calculate_churn_score(
    price_risk,
    trust_risk,
    service_risk,
    transparency_risk,
    alternative_risk,
):
    risks = {
        "price_risk": price_risk,
        "trust_risk": trust_risk,
        "service_risk": service_risk,
        "transparency_risk": transparency_risk,
        "alternative_risk": alternative_risk,
    }
    for value in risks.values():
        _validate_score(value)

    score = sum(risks[k] * WEIGHTS[k] for k in WEIGHTS)
    return round(score, 2)

def get_risk_level(score):
    if score >= 75:
        return "High"
    if score >= 50:
        return "Medium"
    return "Low"
