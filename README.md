# visual-learning-assessment

## TODO

- create informative targetWord plots
- plot highest variance items

## Responses

1.

We have a CSV file with four columns. First we import the CSV using the Pandas library, which provides a convenient system for interacting with tabular data. I will use the Seaborn visualization library (instead of Matplotlib) for its nice default designs and ease of setup.

I like to use the Conda package manager to create environments for each project I start.

2.

The example video consists of first-person footage of a child in a natural environment as well as audio of simultaneous interactions with other humans. Depending on the goal of our analysis, different video processing systems are appropriate.

For this assessment, I decided to implement a video captioning system. I began by exploring literature and articles on current state-of-the-art multimodal video captioning. For this type of data, we ideally have a system that integrates audio and video data to make sense of the scene. The choice of system depends on multiple factors, including available hardware, project budget, our goals for the output, and the setup complexity.

I tested two different methods for video captioning: the open-source [Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni) and the Google Gemini API. I was specifically interested in multi-modal systems (combining audio and video) to provide the richest descriptions.

Using Qwen3-Omni in production would require setting up a GPU server. For this task, I was able to implement programmable tests using the HuggingFace demo platform and the Gradio API.

!!!!!![TODO]: explain the qwen and gemini video caption outputs and compare with the true video

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

3.

> "Hey Émile! Thank you for sharing those details. I've investigated the most likely cause of the issue. Fortunately, my best guess is that your files are safe and we'll be able to fix this soon. I will check with the server admin so we can restore your access to the missing directories. In the meantime, however, just in case we have other issues or you need access to something urgently: are you able to continue working on a different portion of the paper while we fix the issue? If you have backups on your local device or Google Drive of the most essential files, it will be helpful to focus on what you can accomplish with those so that you don't get stuck. Also, let's avoid applying chmod 777 to prevent other issues. Once I confirm the cause, I'll offer guidance on how to prevent this in the future!

> If you need something immediately that you can't find, we can also check with Jane, Haoyu, or one of the other collaborators for the paper since they may have copies available. Please let me know if anything else could be helpful while we resolve the server issue.

> To share context on the problem: Using 'chmod777' grants total permissions to any user, which the server can flag as a security issue. This usually means the directories are automatically moved or access is revoked to prevent cyberattacks or unwanted file overwrites."

Analysis: My first step is to investigate the issue and explore the most likely causes. My next priority is to offer Émile practical steps so they can move forward, which will be helpful regardless of the underlying issue. I also aim to offer whatever honest reassurance I can to alleviate unhelpful stress or anxiety about the problem. I share the most essential details about the cause of the issue so that Émile can have some insight, but it isn't my emphasis.

It's possible that the issue is more complex or uncertain to resolve than I anticipated. As soon as I discovered that, my next step would be to meet with Émile. I'd gather more information on what happened before the directories disappeared and we would carefully explore what Émile needs to meet their deadline. With that context, I could propose more specific strategies for recovering from the data-loss or advise them to request an extension if that becomes necessary.

4.
