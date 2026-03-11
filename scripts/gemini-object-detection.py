from google import genai
from google.genai import types

from dotenv import load_dotenv

load_dotenv()

video_file_name = "../task-data/q2_videodescriptives/faces.png"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='image/png')
            ),
            types.Part(text='Return bounding boxes for all the human faces in the following format as a list. [ymin, xmin, ymax, xmax]')
        ]
    )
)
print(response.text)