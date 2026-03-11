"""
    Created by Ra Mour
    March 9, 2026

    This script runs an input video through the Gemini API, requesting a description of the contents. It outputs the responses to a folder in the data-output directory.
"""

from google import genai
from google.genai import types

from dotenv import load_dotenv

from datetime import datetime
from pathlib import Path


load_dotenv() # load the file that contains the gemini api key


video_file_name = "../task-data/q2_videodescriptives/example_clip.mov"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mov')
            ),
            types.Part(text='You are captioning videos of natural experiences of children. The videos are produced using head-mounted cameras as a child explores their environment. Explain what is happening in each distinct moment of the video. Include the conversations in the video with timestamps as part of the description.')
        ]
    )
)

output_dir = Path(__file__).parent.parent / 'data-output' / 'gemini-video-captions'
output_dir.mkdir(exist_ok=True) # create the output directory if it doesn't exist

filename = output_dir / f"gemini_video_caption{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt" # save text file marked by timestamp

print(response.text)

with open(filename, "w") as f:
    f.write(response.text)
