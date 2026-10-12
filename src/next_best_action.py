def recommend_action(persona: str, journey_stage: str, risks: dict | None = None) -> str:
    persona = persona or ""
    risks = risks or {}

    if "價格" in persona and journey_stage in {
        "Stage 2 - Doubt", "Stage 3 - Comparison", "Stage 4 - Alternative Search"
    }:
        return "提供「必要／建議／可延後」維修項目分級與價格透明說明，必要時由服務顧問主動解釋。"

    if "信任" in persona and journey_stage in {
        "Stage 3 - Comparison", "Stage 4 - Alternative Search", "Stage 5 - Churn"
    }:
        return "安排第二技師意見、說明診斷依據，並由服務顧問主動聯繫追蹤。"

    if "時間" in persona:
        return "提供快速保養時段、預估完工時間與即時維修進度。"

    if "過保" in persona:
        return "提供過保車主專屬分級保養方案，強調原廠履歷、零件與保固價值。"

    if risks.get("alternative_risk", 0) >= 80:
        return "優先處理替代方案意圖：說明原廠總價值並安排顧問式服務，而非只推折扣。"

    return "提供個人化服務說明，並持續觀察後續互動與回廠意圖。"
