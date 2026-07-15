import random
from datetime import datetime

def generate_ticket():

    date = datetime.now().strftime("%Y%m%d")

    number = random.randint(1000, 9999)

    ticket_id = f"CS-{date}-{number}"

    return ticket_id


def escalation_message():

    ticket = generate_ticket()

    return f"""
🚨 Your query requires assistance from a human support agent.

**Ticket ID:** {ticket}

📧 Support Email: support@technova.com

⏰ Response Time: Within 24 Hours

Thank you for your patience.
"""