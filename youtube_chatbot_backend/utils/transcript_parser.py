from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from typing import List,Dict

def get_transcript(video_id:str):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
        return transcript
    except TranscriptsDisabled:
        raise Exception(f"Transcripts are disabled for video ID: {video_id}")
    except NoTranscriptFound:
        raise Exception(f"No transcript found for video ID: {video_id}")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")


def merge_transcript(transcript: List[Dict[str, str]]) -> str:
    return " ".join([seg['text'] for seg in transcript])


