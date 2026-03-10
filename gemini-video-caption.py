from google import genai
from google.genai import types

from dotenv import load_dotenv

load_dotenv()

video_file_name = "task-data/q2_videodescriptives/example_clip.mov"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mov')
            ),
            types.Part(text='You are captioning videos of natural experiences of children. The videos are produced using head-mounted cameras as a child explores their environment. Include the conversations in the video with timestamps as part of the description.')
        ]
    )
)
print(response.text)