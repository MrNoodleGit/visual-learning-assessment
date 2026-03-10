# visual-learning-assessment

## TODO

- create informative targetWord plots
- plot highest variance items

## Responses

1. We have a CSV file with four columns. First we import the CSV using the Pandas library, which provides a convenient system for interacting with tabular data. I will use the Seaborn visualization library (instead of Matplotlib) for its nice default designs and ease of setup.

I like to use the Conda package manager to create environments for each project I start.

2. Model choices: Qwen3-Omni on HuggingFace or MoonDream? or the Gemini API.

The example video consists of first-person footage of a child in a natural environment as well as audio of simultaneous interactions with other humans. Depending on the goal of our analysis, different video processing systems are appropriate.

For this assessment, I decided to implement a video captioning system. I began by exploring literature and articles on current state-of-the-art multimodal video captioning. For this type of data, we ideally have a system that integrates audio and video data to make sense of the scene. The choice of system depends on multiple factors, including available hardware, project budget, our goals for the output, and the setup complexity.

Another interesting approach would be object detection. We may wish to detect the location and category of salient objects in the environment (e.g. books, toys, people) to integrate with eye-tracking data. This would help us answer the question "what tends to attract the toddler's attention at any given moment?". We could compare the outcome in different settings, modifying the activities the child engages in before or during the experiment to explore how that affects their attention patterns.

3. "Hey Émile! Thank you for sharing those details. I've investigated the most likely cause of the issue. Fortunately, my best guess is that your files are safe and we'll be able to fix this soon. I will check with the server admin so we can restore your access to the missing directories. In the meantime, however, just in case we have other issues or you need access to something urgently: are you able to continue working on a different portion of the paper while we fix the issue? If you have backups on your local device or Google Drive of the most essential files, it will be helpful to focus on what you can accomplish with those so that you don't get stuck. Also, let's avoid applying chmod 777 to prevent other issues. Once I confirm the cause, I'll offer guidance on how to prevent this in the future!

If you need something immediately that you can't find, we can also check with Jane, Haoyu, or one of the other collaborators for the paper since they may have copies available. Please let me know if anything else could be helpful while we resolve the server issue.

To share context on the problem: Using 'chmod777' grants total permissions to any user, which the server can flag as a security issue. This usually means the directories are automatically moved or access is revoked to prevent cyberattacks or unwanted file overwrites."

Analysis: My first step is to investigate the issue and explore the most likely causes. My next priority is to offer Émile practical steps so they can move forward, which will be helpful regardless of the underlying issue. I also aim to offer whatever honest reassurance I can to alleviate unhelpful stress or anxiety about the problem. I share the most essential details about the cause of the issue so that Émile can have some insight, but it isn't my emphasis.

Even if unlikely, it's possible that the issue is more complex or uncertain to resolve than I anticipated. As soon as I discovered that, my next step would be to meet with Émile. I'd gather more information on what happened before the directories disappeared and we would carefully explore what Émile needs to meet their deadline. With that context, I could propose more specific strategies for recovering from the data-loss or advise them to request an extension if that becomes necessary.

4.
