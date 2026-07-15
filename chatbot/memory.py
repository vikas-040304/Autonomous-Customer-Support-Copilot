def build_chat_history(messages, limit=6):
    history = ""

    for msg in messages[-limit:]:
        role = msg["role"].capitalize()
        history += f"{role}: {msg['content']}\n"

    return history