import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_groq(question, context):

    prompt = f"""
You are a professional customer support assistant.

Answer ONLY using the company knowledge below.

If the answer is not available, reply:

"I don't have enough information. Your query will be escalated to a human support agent."

Company Knowledge:

{context}

Customer Question:

{question}
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=512
    )

    return completion.choices[0].message.content