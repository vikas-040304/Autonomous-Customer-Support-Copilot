import smtplib
from email.mime.text import MIMEText


def send_email(ticket_id, question, priority):

    sender = "your_email@gmail.com"
    password = "your_app_password"

    receiver = "your_email@gmail.com"

    subject = f"🚨 New Ticket: {ticket_id}"

    body = f"""
New Support Ticket

Ticket ID : {ticket_id}

Priority : {priority}

Question :

{question}
"""

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender, password)

    server.send_message(msg)

    server.quit()