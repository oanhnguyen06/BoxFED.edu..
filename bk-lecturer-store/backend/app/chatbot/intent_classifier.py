def detect_intent(text: str):
    text = text.lower()
    if "ngành" in text:
        return "major"
    if "giảng viên" in text or "thầy" in text or "cô" in text:
        return "lecturer"
    return "other"

