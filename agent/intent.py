def detect_intent(user_input):
    text = user_input.lower()

    if any(x in text for x in ["buy", "start", "subscribe", "try"]):
        return "high_intent"

    if any(x in text for x in ["price", "pricing", "plan", "cost"]):
        return "pricing"

    if any(x in text for x in ["hi", "hello", "hey"]):
        return "greeting"

    return "general"