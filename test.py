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

video_id= "Gfr50f6ZBvo" 
print(f"\n--- Attempting to get transcript for {video_id}")
transcript_data = get_video_transcript(video_id)
if transcript_data:
    print(f"Successfully retrieved transcript for {video_id}. First few segments:")
    for segment in transcript_data[:3]:
        print(segment['text'])
else:
    print(f"Could not retrieve transcript for {video_id}.")


# # --- Test with your successful video_id ---
# video_id_working = "dQw4w9WgXcQ" # Example of a video that likely has a transcript
# print(f"\n--- Attempting to get transcript for {video_id_working} ---")
# transcript_data = get_video_transcript(video_id_working)
# if transcript_data:
#     # Process your transcript data here (e.g., join text for RAG)
#     # print(transcript_data) # Uncomment to see the full transcript structure
#     print(f"Successfully retrieved transcript for {video_id_working}. First few segments:")
#     for segment in transcript_data[:3]:
#         print(segment['text'])
# else:
#     print(f"Could not retrieve transcript for {video_id_working}.")

# # --- Test with a video_id that might cause an error ---
# # Find a YouTube video that you know doesn't have captions, or try a random short one
# # For example, a very new upload, or a small channel's video.
# video_id_failing = "g8A_L_W2m_U" # Replace with a video ID that fails for you, e.g., a random one without captions
# print(f"\n--- Attempting to get transcript for {video_id_failing} ---")
# transcript_data_failing = get_video_transcript(video_id_failing)
# if transcript_data_failing:
#     print(f"Successfully retrieved transcript for {video_id_failing}.")
#     for segment in transcript_data_failing[:3]:
#         print(segment['text'])
# else:
#     print(f"Could not retrieve transcript for {video_id_failing}.")
