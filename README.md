# MediMind 💬 – AI-Powered Medical Assistant Chatbot

MediMind is an AI-powered chatbot that helps users describe and understand their symptoms through a user-friendly conversational interface. It uses Groq's LLaMA 3 model for intelligent medical conversations and Firebase to store chat history securely.

---

## 🌐 Live Demo

➡️(https://medimind-3.onrender.com/)

---

## ✨ Features

* 🔦 Conversational AI using Groq LLaMA 3
* 🔐 Firebase Anonymous Authentication
* 💬 Real-time Chat with UI Message Bubbles
* ☁️ Chat History Stored with Firestore
* ✏️ Single-question follow-up logic for better diagnosis
* 🌍 Deployed frontend + backend on Render

---

## 📁 Folder Structure

```
medimind/
├── medimind-frontend/
│   ├── index.html
│   └── index.js
│
├── medimind-backend/
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

---

## ⚙️ Tech Stack

* Groq API (LLaMA 3 Model)
* Firebase Firestore + Authentication
* Flask (Python Backend)
* HTML/CSS/JavaScript (Frontend)
* Render (Deployment Platform)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/medimind.git
cd medimind
```

### 2. Backend Setup

```bash
cd medimind-backend
pip install -r requirements.txt
python app.py
```

### 3. Frontend Setup

* Open `medimind-frontend/index.html` in a browser
* Ensure Firebase config is set inside the `<script>` section of `index.html`

---

## 🚀 How It Works

1. User describes a symptom in the chatbot.
2. Message is saved to Firebase Firestore.
3. Message sent to Groq's API (LLaMA 3).
4. Chatbot replies with medically guided question.
5. Response is shown on UI and saved to history.

---

## 💼 Deployment

This project is fully deployed using **Render**:

* Flask backend serves frontend and handles chat endpoint.
* Frontend (HTML/JS) communicates directly with Firebase and the `/chat` endpoint.

---

## 👤 Author

Built with passion by **Muskan Singh**
Let me know if you want to collaborate or extend the project!

---

## 📢 Feedback & Contributions

Feel free to fork this project, suggest features, or open issues. Contributions are welcome!
