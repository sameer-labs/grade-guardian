from pydantic import BaseModel

class YoutubeTranscript(BaseModel):
    video_id: str
    language: str = "en"
    snippets_count: int
    duration_seconds: int

transcript = YoutubeTranscript(
    video_id="dQw4w9WgXcQ",
    snippets_count="47",
    duration_seconds=213
)

print(transcript)
print(f" Video is {transcript.duration_seconds // 60} minutes long")
