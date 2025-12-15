from .intent_classifier import detect_intent
from .rules import MAJOR_INFO

def answer_question(message: str):
    intent = detect_intent(message)

    if intent == "major":
        for k, v in MAJOR_INFO.items():
            if k in message.lower():
                return v
        return "Bạn muốn hỏi về ngành nào của HUST?"

    if intent == "lecturer":
        return "Bạn có thể xem danh sách giảng viên theo khoa trên website."

    return "Mình có thể hỗ trợ bạn về ngành học hoặc giảng viên HUST."

