import streamlit as st
from chatbot.dashboard import get_metrics
from chatbot.ticket_dashboard import get_all_tickets

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Analytics Dashboard")

# -----------------------
# Feedback Metrics
# -----------------------

helpful, not_helpful, total, satisfaction = get_metrics()

col1, col2, col3, col4 = st.columns(4)

col1.metric("👍 Helpful", helpful)
col2.metric("👎 Not Helpful", not_helpful)
col3.metric("📈 Total Feedback", total)
col4.metric("😊 Satisfaction", f"{satisfaction}%")

st.divider()

# -----------------------
# Ticket Metrics
# -----------------------

tickets = get_all_tickets()

st.subheader("🎫 Ticket Summary")

if not tickets.empty:

    open_count = len(
        tickets[tickets["Status"] == "Open"]
    )

    closed_count = len(
        tickets[tickets["Status"] == "Closed"]
    )

    c1, c2 = st.columns(2)

    c1.metric(
        "Open Tickets",
        open_count
    )

    c2.metric(
        "Closed Tickets",
        closed_count
    )

    st.bar_chart(
        tickets["Category"].value_counts()
    )

else:

    st.info("No tickets found.")