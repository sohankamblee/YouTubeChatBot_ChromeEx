# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from youtube_chatbot_backend.utils.transcript_parser import get_transcript, merge_transcript
from youtube_chatbot_backend.rag_pipeline import get_chat_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat_endpoint(request: Request):
    body = await request.json()
    video_id = body.get("video_id")
    user_input = body.get("user_input")

    if user_input.strip().lower() == "exit":
        return {"response": "Chatbot session ended."}
    
    try:
        transcript = get_transcript(video_id)
        context = merge_transcript(transcript)
        answer = get_chat_response(context, user_input)
        return {"response": answer}
    except Exception as e:
        print("Backend error:", str(e))
        return {"error": str(e)}