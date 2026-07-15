def detect_intent(question):

    question = question.lower()

    if any(word in question for word in ["hi", "hello", "hey"]):
        return "Greeting"

    elif any(word in question for word in ["password", "forgot password", "reset"]):
        return "Password Reset"

    elif any(word in question for word in ["refund", "return", "money back"]):
        return "Refund Request"

    elif any(word in question for word in ["payment", "upi", "credit", "debit"]):
        return "Payment Query"

    elif any(word in question for word in ["order", "track"]):
        return "Order Status"

    elif any(word in question for word in ["delete account", "remove account"]):
        return "Account Deletion"

    elif any(word in question for word in ["business hours", "working hours", "timing"]):
        return "Business Hours"

    else:
        return "Unknown"