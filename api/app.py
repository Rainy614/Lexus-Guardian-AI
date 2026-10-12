from flask import Flask, jsonify, request, render_template

from src.preprocess import normalize_text
from src.risk_scoring import calculate_churn_score, get_risk_level
from src.churn_journey import classify_journey_stage, detect_primary_trigger
from src.next_best_action import recommend_action

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "Lexus Guardian AI Prototype"})

@app.post("/analyze")
def analyze():
    payload = request.get_json(silent=True) or {}
    required = [
        "text", "price_risk", "trust_risk", "service_risk",
        "transparency_risk", "alternative_risk",
    ]
    missing = [k for k in required if k not in payload]
    if missing:
        return jsonify({"error": "missing fields", "fields": missing}), 400

    text = normalize_text(payload["text"])
    persona = payload.get("persona", "未分類")
    risks = {
        "price_risk": float(payload["price_risk"]),
        "trust_risk": float(payload["trust_risk"]),
        "service_risk": float(payload["service_risk"]),
        "transparency_risk": float(payload["transparency_risk"]),
        "alternative_risk": float(payload["alternative_risk"]),
    }

    try:
        score = calculate_churn_score(**risks)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    stage = classify_journey_stage(text)
    return jsonify({
        "persona": persona,
        "churn_score": score,
        "risk_level": get_risk_level(score),
        "journey_stage": stage,
        "primary_trigger": detect_primary_trigger(text),
        "next_best_action": recommend_action(persona, stage, risks),
        "risk_dimensions": risks,
        "prototype_note": "v0.3 heuristic prototype; not production calibrated",
    })

if __name__ == "__main__":
    app.run(debug=True, port=7000)
