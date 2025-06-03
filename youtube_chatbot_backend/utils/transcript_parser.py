from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

video_id = ''
try:
    # If you don’t care which language, this returns the “best” one
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])

    # Flatten it to plain text
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    #print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video.")

