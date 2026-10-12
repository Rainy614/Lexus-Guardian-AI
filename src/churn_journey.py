def classify_journey_stage(text: str) -> str:
    text = (text or "").lower()

    if any(k in text for k in ["不回原廠", "不會再回原廠", "以後不回原廠", "改去外廠", "已經不回原廠"]):
        return "Stage 5 - Churn"

    if any(k in text for k in ["外廠", "lexus 專修", "lexus專修", "民間保養", "推薦保養廠"]):
        return "Stage 4 - Alternative Search"

    if any(k in text for k in ["比較", "外面比較便宜", "cp值", "cp 值"]):
        return "Stage 3 - Comparison"

    if any(k in text for k in ["真的需要換", "有必要換", "為什麼要換", "是不是一定要換", "叫我換一堆", "被叫我換"]):
        return "Stage 2 - Doubt"

    if any(k in text for k in ["太貴", "變貴", "越來越貴", "報價很高", "保養費"]):
        return "Stage 1 - Complaint"

    return "Stage 0 - Stable"

def detect_primary_trigger(text: str) -> str:
    text = (text or "").lower()

    if any(k in text for k in ["外廠", "lexus 專修", "lexus專修", "民間保養"]):
        return "Active search for alternative service"
    if any(k in text for k in ["沒修好", "修不好", "問題沒解決", "一直說正常"]):
        return "Unresolved service issue / trust decline"
    if any(k in text for k in ["有必要換", "為什麼要換", "叫我換一堆", "被叫我換"]):
        return "Repair necessity / transparency concern"
    if any(k in text for k in ["太貴", "變貴", "報價", "保養費"]):
        return "Price dissatisfaction"
    return "No dominant trigger detected"
