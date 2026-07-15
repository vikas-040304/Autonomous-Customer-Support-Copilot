import random
from datetime import datetime


def create_ticket(priority="Medium", category="General"):

    ticket_id = f"TK-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000,9999)}"

    message = f"""
🎫 **Support Ticket Created**

**Ticket ID:** {ticket_id}

**Category:** {category}

**Priority:** {priority}

**Status:** Open

Our support team will contact you shortly.
"""

    print(ticket_id, message)

    return ticket_id, message