from gradio_client import Client, handle_file

client = Client("Qwen/Qwen3-Omni-Demo") # load Gradio Qwen Omni demo client

response = client.predict(
  audio=None,
  video={"video":handle_file('task-data/q2_videodescriptives/example_clip.mov'),"subtitles":None},
  history=[],
  system_prompt="You are captioning videos of natural experiences of children. The videos are produced using head-mounted cameras as a child explores their environment. Include the conversations in the video with timestamps as part of the description.",
  voice_choice="Cherry / 芊悦",
  temperature=0.6,
  top_p=0.95,
  top_k=20,
  return_audio=False,
  enable_thinking=True,
  api_name="/media_predict"
)

print(response)
