# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from youtube_chatbot_backend.utils.transcript_parser import get_transcript, merge_transcript
from youtube_chatbot_backend.rag_pipeline import get_chat_response
#from pydantic import BaseModel
import logging
import time

app = FastAPI()


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global cache
transcript_cache = {}

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

def get_transcript_with_retry(video_id: str, retries: int = 2, delay: float = 2.0):
    for attempt in range(retries):
        try:
            logging.info(f"Fetching transcript for video_id={video_id}, attempt {attempt + 1}")
            return get_transcript(video_id)
        except Exception as e:
            logging.warning(f"Transcript fetch attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise

@app.post("/chat")
async def chat_endpoint(request: Request):
    try:
        body = await request.json()
    except Exception as e:
        logging.error(f"Failed to parse JSON body: {e}")
        return {"error": "Invalid JSON in request body."}

    video_id = body.get("video_id")
    user_input = body.get("user_input")

    logging.info(f"Received request with video_id={video_id} and user_input={user_input}")

    if not video_id or not user_input:
        return {"error": "Missing video_id or user_input in request."}

    if user_input.strip().lower() == "exit":
        return {"response": "Chatbot session ended."}

    try:
        # Use cached transcript if available
        if video_id in transcript_cache:
            transcript = transcript_cache[video_id]
            logging.info(f"Transcript for video_id={video_id} loaded from cache.")
        else:
            transcript = get_transcript_with_retry(video_id)
            transcript_cache[video_id] = transcript
            logging.info(f"Transcript for video_id={video_id} fetched and cached.")

        if not transcript:
            logging.warning(f"No transcript found for video_id={video_id}")
            return {"error": f"No transcript found for video_id: {video_id}"}

        context = merge_transcript(transcript)
        answer = get_chat_response(context, user_input)
        return {"response": answer}

    except Exception as e:
        logging.error(f"Backend error: {str(e)}")
        return {"error": f"An error occurred: {str(e)}"}