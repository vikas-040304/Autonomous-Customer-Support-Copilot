import streamlit as st
from chatbot.admin_auth import login
from chatbot.ticket_dashboard import get_all_tickets
from chatbot.ticket_admin import update_ticket_status
from chatbot.export import export_csv, export_excel

# -----------------------------------
# Session
# -----------------------------------

if "admin" not in st.session_state:
    st.session_state.admin = False

# -----------------------------------
# Login
# -----------------------------------

if not st.session_state.admin:

    login()

    st.stop()

# -----------------------------------
# Dashboard
# -----------------------------------

st.title("🎫 Admin Ticket Dashboard")

st.success("✅ Logged in as Admin")

tickets = get_all_tickets()

if tickets.empty:

    st.info("No tickets found.")

else:

    open_count = len(
        tickets[tickets["Status"] == "Open"]
    )

    closed_count = len(
        tickets[tickets["Status"] == "Closed"]
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "🟢 Open Tickets",
        open_count
    )

    col2.metric(
        "🔴 Closed Tickets",
        closed_count
    )
    st.divider()

col1, col2 = st.columns(2)

with col1:

    csv_file = export_csv(tickets)

    with open(csv_file, "rb") as f:

        st.download_button(
            "📄 Export CSV",
            data=f,
            file_name=csv_file,
            mime="text/csv"
        )

with col2:

    excel_file = export_excel(tickets)

    with open(excel_file, "rb") as f:

        st.download_button(
            "📊 Export Excel",
            data=f,
            file_name=excel_file,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

st.divider()


st.divider()

for _, row in tickets.iterrows():

    with st.expander(
        f"{row['Ticket ID']} | {row['Question']}"
    ):

        st.write(
            f"**Category:** {row['Category']}"
        )

        st.write(
            f"**Priority:** {row['Priority']}"
        )

        st.write(
            f"**Status:** {row['Status']}"
        )

        if row["Status"] == "Open":

            if st.button(
                "✅ Close Ticket",
                key=row["Ticket ID"]
            ):

                update_ticket_status(
                    row["Ticket ID"],
                    "Closed"
                )

                st.success(
                    "Ticket Closed Successfully"
                )

                st.rerun()

st.divider()

if st.button("🚪 Logout"):

    st.session_state.admin = False

    st.rerun()