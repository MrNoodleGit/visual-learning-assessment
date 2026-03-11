# 2. Video Descriptives

The example video consists of first-person footage of a child in a natural environment as well as audio of simultaneous interactions with other humans. Depending on the goal of our analysis, different video processing systems are appropriate. For this assessment, I tested two different approaches that could be plausibly useful for projects in the visual learning lab.

## Video Captioning using multimodal reasoning models

I first implemented a video captioning system. I began by exploring literature and articles on current state-of-the-art multimodal video captioning. For this type of data, we ideally have a system that integrates audio and video data to make sense of the scene. The choice of system depends on multiple factors, including available hardware, project budget, our goals for the output, and the setup complexity.

I tested two different methods for video captioning: the open-source [Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni) and the Google Gemini API. I was specifically interested in multi-modal systems (combining audio and video) to provide the richest descriptions.

Using Qwen3-Omni in production would require setting up a GPU server. For this task, I was able to implement programmable tests using the HuggingFace demo platform and the Gradio API.

For my description of the outputs, I'll focus on the Gemini video captions. I instructed the model to include conversations in its response to, both to have a transcript for reference and to help it use the audio information to generate a detailed description.

gemini_video_caption_1.md shows an impressive response from the gemini-2.5-flash reasoning model. It provides a detailed, accurate description of each moment in the video. I set the model to examine the video at 1 frame per second, which is enough for this type of content. Since it iterates through frames, the model is able to examine the scene in greater specific detail than a human could. For instance, it can discern the specific titles of books that would be difficult to recognize for a person viewing in real-time.

However, in this response the model didn't report the mother's first words in the video. A different run (gemini_video_caption20260310_214737.txt) using Gemini-3-Flash-Preview captures the missing sentence--"Ooh, maybe you want to see the Bear's Birthday book?"--but it doesn't provide a detailed account of the video moment by moment.

An characteristic feature of generative AI models is their probabilistic behavior. Different runs of the same instructions, on the same inputs, will usually produce significantly different responses unless the model is forced to give a structured output. Effective use of this type of models requires a fair amount of testing with different prompts to obtain the desired results. It also requires verification testing to ensure that the model will behave as expected in most production runs.

## Face Detection to study the effects of technology of child development

Another interesting approach is object detection. We may wish to detect the location and category of salient objects in the environment (e.g. books, toys, people) to integrate with eye-tracking data. This would help us answer the question "what tends to attract the toddler's attention at any given moment?". We could compare the outcome in different settings, modifying the activities the child engages in before or during the experiment to explore how that affects their attention patterns.

It is worth asking, "what are the effects of technology exposure to the development of young children?" Faces are arguably the most important objects that children encounter throughout their development. Object detection combined with eye-tracking could allow us to investigate the effect of technology on children's orientation toward faces, which serves as an important indicator of social attunement.

I implemented a face detection script to demonstrate a simple proof of concept. I explored several methods for accomplishing this, including the [Google Gemini API](https://ai.google.dev/gemini-api/docs/video-understanding) (general intelligence model), the [Moondream Vision AI](https://moondream.ai/) platform, and several open-source computer vision libraries that are specifically optimized for face detection.

My goal was to generate bounding boxes that identified the faces in each frame of the example video. Then, I could produce a new video that showed the face area in each frame. This involved several challenges. First, the detection system would have to be fast enough to process entire videos, not just a few images. It also had to be accurate and reliable.

I was curious to see how effective Gemini was for this task. In addition to many other tasks, Gemini is also [explicitly trained on object detection](https://ai.google.dev/gemini-api/docs/image-understanding#object-detection). Noteably, we can ask it to generate bounding box coordinates through direct prompting:

> 'Return bounding boxes for all the human faces in the following format as a list. [ymin, xmin, ymax, xmax]'

```[
  {"box_2d": [306, 508, 431, 712], "label": "the adult woman"},
  {"box_2d": [363, 489, 435, 563], "label": "the small child"}
]
```

However, the inference time to use Gemini to annotate entire videos is infeasible. It also requires strict prompting to attempt to force the model to always give the desired output structure. It is like using a bulldozer to place a nail.

In the end, I settled on the [RetinaFace](https://github.com/serengil/retinaface) computer vision python library. This is a very high accuracy computer vision model trained exclusively to detect faces. I was able to detect faces for every single frame and draw the bounding boxes in ~1 - 2 minutes of compute (for a 17 second video) using the Google Colab T4 GPU. I implented the logic to load the video, draw the bounding boxes, and export using the [OpenCV library](https://docs.opencv.org/4.x/).
