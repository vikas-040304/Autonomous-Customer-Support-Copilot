from datetime import datetime

def export_chat(messages):
    filename = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for msg in messages:
            file.write(f"{msg['role'].upper()}:\n")
            file.write(msg["content"])
            file.write("\n\n")

    return filename