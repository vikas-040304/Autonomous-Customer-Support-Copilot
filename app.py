import streamlit as st
from chatbot.rag import create_vector_db
from chatbot.llm import ask_groq
from chatbot.intents import detect_intent
from chatbot.escalation import escalation_message
from chatbot.feedback import init_db, save_feedback
from chatbot.dashboard import get_metrics
from chatbot.pdf_loader import load_pdf
from utils.helper import export_chat
from chatbot.memory import build_chat_history
from chatbot.orders import init_orders
from chatbot.order_handler import check_order_query
from chatbot.ticket import create_ticket
from chatbot.ticket_db import init_ticket_db, save_ticket
from chatbot.ticket_dashboard import get_all_tickets


st.set_page_config(
    page_title="Autonomous Customer Support Copilot",
    page_icon="🤖",
    layout="wide"
)

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🤖 Autonomous Customer Support Copilot")

# =====================================
# Session State
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "db" not in st.session_state:
    init_db()
    init_orders()
    init_ticket_db()
    st.session_state.db = create_vector_db()

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.header("⚙️ Settings")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    # -------------------------
    # Download Chat
    # -------------------------

    if st.session_state.messages:

        file = export_chat(st.session_state.messages)

        with open(file, "rb") as f:

            st.download_button(
                "📥 Download Chat",
                data=f,
                file_name=file,
                mime="text/plain"
            )

    st.divider()

    # -------------------------
    # Upload PDF
    # -------------------------

    st.subheader("📂 Upload Knowledge Base")

    uploaded_file = st.file_uploader(
        "Upload Company PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        pdf_text = load_pdf(uploaded_file)

        with open(
            "data/company_knowledge.txt",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(pdf_text)

        st.session_state.db = create_vector_db()

        st.success("✅ PDF uploaded successfully!")

    st.divider()

    # -------------------------
    # Resolution Metrics
    # -------------------------

    st.subheader("📊 Resolution Metrics")

    helpful, not_helpful, total, satisfaction = get_metrics()

    st.metric("👍 Helpful", helpful)
    st.metric("👎 Not Helpful", not_helpful)
    st.metric("📈 Total", total)
    st.metric("😊 Satisfaction", f"{satisfaction}%")

# =====================================
# MAIN PAGE
# =====================================

st.subheader("🎫 Ticket Dashboard")

tickets = get_all_tickets()

if not tickets.empty:

    search = st.text_input("🔍 Search Ticket")

    if search:

        tickets = tickets[
            tickets.astype(str)
            .apply(
                lambda row: row.str.contains(
                    search,
                    case=False
                ).any(),
                axis=1
            )
        ]

    status = st.selectbox(
        "Filter Status",
        ["All", "Open", "Closed"]
    )

    if status != "All":
        tickets = tickets[
            tickets["Status"] == status
        ]

    st.dataframe(
        tickets,
        use_container_width=True
    )

else:

    st.info("No tickets found.")

st.divider()

# =====================================
# CHAT
# =====================================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

prompt = st.chat_input("Ask your question...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    docs = st.session_state.db.similarity_search(
        prompt,
        k=3
    )

    knowledge = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    history = build_chat_history(
        st.session_state.messages
    )

    context = f"""
Previous Conversation:
{history}

Knowledge Base:
{knowledge}
"""

    intent = detect_intent(prompt)

    with st.chat_message("assistant"):

        st.caption(
            f"🎯 Detected Intent: {intent}"
        )

        with st.spinner("Thinking..."):

            # --------------------------------
            # Order Tracking
            # --------------------------------

            order_response = check_order_query(
                prompt
            )

            if order_response:

                answer = order_response

            else:

                answer = ask_groq(
                    prompt,
                    context
                )

            # --------------------------------
            # Escalation
            # --------------------------------

            if (
                "I don't have enough information"
                in answer
            ): # type: ignore

                answer += "\n\n" # type: ignore

                answer += escalation_message()

                ticket_id, ticket_message = create_ticket(
                    priority="Medium",
                    category=intent
                )

                save_ticket(
                    ticket_id,
                    prompt,
                    intent,
                    "Medium"
                )

                answer += "\n\n"

                answer += ticket_message

            st.markdown(answer)

            col1, col2 = st.columns(2)

            with col1:
                if st.button(
                    "👍 Helpful",
                    key=f"up_{len(st.session_state.messages)}"
                ):
                    save_feedback(
                        prompt,
                        answer,
                        "Helpful"
                    )
                    st.success("Thank you for your feedback!")

            with col2:
                if st.button(
                    "👎 Not Helpful",
                    key=f"down_{len(st.session_state.messages)}"
                ):
                    save_feedback(
                        prompt,
                        answer,
                        "Not Helpful"
                    )
                    st.warning("Feedback recorded.")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )