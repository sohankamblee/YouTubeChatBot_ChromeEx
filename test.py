from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled, VideoUnavailable

def get_video_transcript(video_id):
    try:
        # Try to get the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except NoTranscriptFound:
        print(f"Error: No transcript found for video ID: {video_id}. It might not have auto-generated or manual captions.")
        return None
    except TranscriptsDisabled:
        print(f"Error: Transcripts are disabled for video ID: {video_id}.")
        return None
    except VideoUnavailable:
        print(f"Error: Video ID: {video_id} is unavailable or private.")
        return None
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred while fetching transcript for video ID {video_id}: {e}")
        return None

video_id= "2gtskGWSgew" 
print(f"\n--- Attempting to get transcript for {video_id}")
transcript_data = get_video_transcript(video_id)
if transcript_data:
    print(f"Successfully retrieved transcript for {video_id}. First few segments:")
    for segment in transcript_data[:3]:
        print(segment['text'])
else:
    print(f"Could not retrieve transcript for {video_id}.")
