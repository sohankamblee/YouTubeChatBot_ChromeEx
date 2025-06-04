# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from youtube_chatbot_backend.utils.transcript_parser import get_transcript, merge_transcript
from youtube_chatbot_backend.rag_pipeline import get_chat_response
#from pydantic import BaseModel
import logging

app = FastAPI()


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging (new)
logging.basicConfig(level=logging.INFO)

@app.get("/env-check")
async def env_check():
    import sys
    import platform
    #import requests
    import socket

    try:
        internet = socket.gethostbyname("youtube.com")
    except:
        internet = "NO INTERNET ACCESS"

    return {
        "python_version": sys.version,
        "platform": platform.platform(),
        "youtube_transcript_api": True,
        "internet_access": internet
    }


@app.post("/chat")
async def chat_endpoint(request: Request):
    try:
        body = await request.json()
    except Exception as e:
        logging.error(f"Failed to parse JSON body: {e}")
        return {"error": "Invalid JSON in request body."}

    video_id = body.get("video_id")
    user_input = body.get("user_input")

    # Log received input (new)
    logging.info(f"Received request with video_id={video_id} and user_input={user_input}")

    # Validate input (new)
    if not video_id or not user_input:
        return {"error": "Missing video_id or user_input in request."}

    if user_input.strip().lower() == "exit":
        return {"response": "Chatbot session ended."}

    try:
        transcript = get_transcript(video_id)

        # Debug log transcript (new)
        if not transcript:
            logging.warning(f"No transcript found for video_id={video_id}")
            return {"error": f"No transcript found for video_id: {video_id}"}

        context = merge_transcript(transcript)
        answer = get_chat_response(context, user_input)
        return {"response": answer}

    except Exception as e:
        logging.error(f"Backend error: {str(e)}")
        return {"error": f"An error occurred: {str(e)}"}
