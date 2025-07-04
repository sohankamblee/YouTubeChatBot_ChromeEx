# 🎥 YouTube Chatbot Extension with RAG (Retrieval-Augmented Generation)

This project is a **Chrome Extension** that lets users **chat with YouTube videos** in real-time using a **local Python backend** powered by **RAG (Retrieval-Augmented Generation)**. The chatbot analyzes the transcript of the video and provides intelligent responses based on the video content, not just pretrained model knowledge.

---

## 📸 Demo

Here's a screenshot of the Chrome Extension in action:

![YouTube Chatbot Demo](assets/screenshot.png)

## 🧠 Features

- Chatbot that answers questions about any YouTube video.
- Chrome extension UI that runs on top of the YouTube page.
- RAG pipeline using video transcripts + LLM for relevant answers.
- Local FastAPI backend for fast and private processing.
- `.env` support for sensitive credentials like your OpenAI API Key.

---

## 📁 Project Structure

```
youtube_chatbot_extension/
│
├── backend/
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── utils/
│   │   └── transcript_parser.py
│   ├── .env             👈 API key is placed here
│   └── requirements.txt
│
├── extension/
│   ├── popup.html
│   ├── popup.js
│   ├── styles.css
│   └── manifest.json
```

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/your-username/youtube-chatbot-extension.git
cd youtube_chatbot_extension/backend
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ Optional: If using FAISS, install `faiss-cpu` or `faiss-gpu` depending on your environment:
```bash
pip install faiss-cpu
# or
pip install faiss-gpu
```

---

### 3. Create a `.env` file (for OpenAI API Key)

Create a `.env` file inside the **`backend/`** folder with the following content:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

### 4. Start the backend server

From inside the `backend/` folder:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server at:  
📡 `http://127.0.0.1:8000/chat`

---

### 5. Load Chrome Extension

1. Open Chrome and go to `chrome://extensions/`
2. Enable **Developer Mode**.
3. Click **"Load Unpacked"**.
4. Select the `extension/` folder from the project directory.
5. Navigate to YouTube and click the extension icon to interact.

---

## ✅ Example Use

1. Play any YouTube video with English subtitles.
2. Ask: *"Summarize the video"*, or *"What did the speaker say about DeepMind?"*
3. Get contextual answers based on the transcript.

---

## 🛠️ Notes

- Make sure the video has a transcript (auto or manual) for proper results.
- The extension sends the current video ID and user query to the backend.
- The backend fetches transcript, applies RAG, and returns an answer.

---

## 🧠 Future Improvements

- Add support for non-English transcripts.
- Cache results to avoid repeated transcript fetching.
- Support conversation memory or follow-up questions.

---
