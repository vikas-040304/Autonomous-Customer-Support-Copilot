# 🤖 Autonomous Customer Support Copilot

An AI-powered Customer Support Chatbot built using **Streamlit, LangChain, Groq LLM, and RAG (Retrieval Augmented Generation)**. The chatbot answers customer queries using a company knowledge base, tracks orders, creates support tickets when necessary, and provides an admin dashboard to manage tickets.

---

## 📌 Project Overview

The Autonomous Customer Support Copilot is designed to automate customer support by providing instant responses to user queries. It uses Retrieval Augmented Generation (RAG) to fetch relevant information from uploaded company documents and generates accurate responses using Groq LLM.

If the chatbot cannot answer a query, it automatically creates a support ticket for human assistance. An Admin Dashboard allows support staff to monitor and close tickets.

---

## ✨ Features

- 🤖 AI-powered Customer Support Chatbot
- 📄 PDF Knowledge Base Upload
- 🔍 RAG-based Information Retrieval
- 💬 Multi-turn Conversation Memory
- 🎯 Intent Detection
- 📦 Order Tracking
- 🎫 Automatic Ticket Generation
- 🔐 Admin Login Authentication
- 📊 Analytics Dashboard
- 👍 User Feedback Collection
- 📥 Chat Export
- 📈 Resolution Metrics

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI & NLP
- LangChain
- Groq LLM
- HuggingFace Embeddings
- FAISS Vector Database

### Database
- SQLite

### Libraries
- Pandas
- PyPDF
- Python-dotenv
- OpenPyXL

---

## 📂 Project Structure

```
Autonomous-Customer-Support-Copilot/
│
├── chatbot/
│   ├── admin_auth.py
│   ├── dashboard.py
│   ├── escalation.py
│   ├── feedback.py
│   ├── intents.py
│   ├── llm.py
│   ├── memory.py
│   ├── order_handler.py
│   ├── orders.py
│   ├── pdf_loader.py
│   ├── rag.py
│   ├── ticket.py
│   ├── ticket_admin.py
│   ├── ticket_dashboard.py
│   └── ticket_db.py
│
├── pages/
│   ├── 🎫_Ticket_Dashboard.py
│   └── 📊_Analytics.py
│
├── database/
├── data/
├── utils/
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Keerthi-1603-M/Autonomous-Customer-Support-Copilot.git
```

Go to the project folder

```bash
cd Autonomous-Customer-Support-Copilot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_api_key
```

Run the application

```bash
streamlit run app.py
```

---

## 🚀 How It Works

1. Upload Company Knowledge PDF.
2. The PDF is converted into embeddings using HuggingFace.
3. FAISS stores vector embeddings.
4. User asks a question.
5. Relevant information is retrieved using RAG.
6. Groq LLM generates the final response.
7. If information is unavailable, a support ticket is automatically created.
8. Admin reviews and closes tickets from the dashboard.

---

## 📸 Screenshots

### Home Page

<img width="1919" height="1078" alt="image" src="https://github.com/user-attachments/assets/749cc254-4bef-4e2f-8cfc-61330549335d" />


### Chatbot Response

<img width="1919" height="1074" alt="image" src="https://github.com/user-attachments/assets/4c1324c3-736b-44e0-a281-4f3547fb4941" />


### Admin Dashboard

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/83868253-6bdd-42a2-82e4-2dd8d33800f5" />


### Ticket Dashboard

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/04be3cd5-43f7-4d3a-9bb5-522a53b82494" />



### Analytics Dashboard

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/0085f482-18de-4b9c-94e3-9133426035ea" />


---

## 📊 Future Enhancements

- Email Notifications
- Voice Assistant
- WhatsApp Integration
- Multi-language Support
- Live Agent Chat
- Cloud Deployment

---

## 👨‍💻 Author

**Keerthi M**

GitHub:
https://github.com/vikas-040304

---

## 📄 License

This project is developed for educational purposes.
