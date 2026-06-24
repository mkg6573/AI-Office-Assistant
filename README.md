# 🎤 AI Meeting Assistant

An AI-powered Smart Office Assistant built that automates meeting workflows by converting audio recordings into transcripts, generating summaries, creating professional follow-up emails, sending emails to team members, and answering questions based on meeting discussions.

---

## 🚀 Features

### 🎙️ Meeting Transcription

* Upload meeting audio files (`.mp3`, `.wav`, `.m4a`)
* Generate accurate meeting transcripts
* Automatic speaker identification
* Clean and readable transcript output

### 📋 AI Meeting Summary

* Generate concise meeting summaries
* Capture key discussion points
* Highlight important decisions
* Extract actionable insights

### 📧 Professional Email Generation

* Create professional follow-up emails automatically
* Summarize meeting outcomes
* Include key decisions and action items
* Corporate-ready email formatting

### 📨 Email Sending

* Send generated emails directly to team members
* Support multiple recipients
* Automated meeting communication

### 💬 AI Meeting Chat

* Ask questions about the meeting
* Get answers directly from the transcript
* Retrieve decisions, action items, deadlines, and discussions
* AI-powered meeting assistant sidebar

---



## 📂 Project Structure

```bash
AI-Meeting-Assistant/
│
├── app.py
├── transcription.py
├── summarizer.py
├── email_generator.py
├── email_sender.py
├── qa.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/mkg6573/AI-Meeting-Assistant.git
cd AI-Meeting-Assistant
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
EMAIL_ADDRESS=YOUR_EMAIL
EMAIL_PASSWORD=YOUR_APP_PASSWORD
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Upload meeting audio.
2. Click **🚀 Process Meeting**.
3. AI generates:

   * Transcript
   * Summary
   * Professional Email
4. Send email to team members.
5. Ask questions using the AI sidebar assistant.

---

## 🎯 Example Questions

* What decisions were made?
* What are the action items?
* Who is responsible for the task?
* What deadlines were discussed?
* What are the next steps?
* Summarize the meeting.

---

## 📸 Workflow

```text
Meeting Audio
      ↓
AI Transcription
      ↓
Meeting Summary
      ↓
Professional Email
      ↓
Email Distribution
      ↓
AI Question Answering
```

---

## 🌟 Future Enhancements

* Task Extraction & Assignment
* Meeting Analytics Dashboard
* PDF Export
* Meeting History Storage
* RAG-based Document Chat
* Multi-language Support
* Calendar Integration

---


## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
