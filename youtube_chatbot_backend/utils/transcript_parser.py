from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from typing import List, Dict, Union
import logging

# Enable debug logging
logging.basicConfig(level=logging.INFO)

def get_transcript(video_id: str) -> List[Dict[str, Union[str, float]]]:
    logging.info(f"Attempting to fetch transcript for video ID: {video_id}")
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
        logging.debug(f"Raw transcript: {transcript}")
        if not transcript:
            raise Exception(f"Empty transcript received for video ID: {video_id}")
        logging.info(f"Transcript fetched successfully for video ID: {video_id}")
        return transcript
    except TranscriptsDisabled:
        logging.error(f"Transcripts are disabled for video ID: {video_id}")
        raise Exception(f"Transcripts are disabled for video ID: {video_id}")
    except NoTranscriptFound:
        logging.error(f"No transcript found for video ID: {video_id}")
        raise Exception(f"No transcript found for video ID: {video_id}")
    except Exception as e:
        logging.error(f"Unexpected error while fetching transcript: {str(e)}")
        raise Exception(f"An error occurred while retrieving transcript: {str(e)}")


def merge_transcript(transcript: List[Dict[str, Union[str, float]]]) -> str:
    if not isinstance(transcript, list) or not all(isinstance(seg, dict) for seg in transcript):
        raise ValueError("Invalid transcript format: Expected a list of dictionaries.")
    
    merged = " ".join(seg.get('text', '') for seg in transcript if 'text' in seg)
    logging.info(f"Merged transcript length: {len(merged)} characters")
    return merged
