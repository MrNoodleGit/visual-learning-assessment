# Lab Coordinator Interview Tasks

Computational Focus
Visual Learning Lab, Winter 2026

## 1. Visualizing data

We would like to measure which words are harder or easier for children to understand. Our pilot study examined how children can recognize certain words (e.g., “apple”) in the presence of a distractor image (e.g., “carrot”). The provided .csv file in the folder “question1” contains averaged binary response data (column name “pc”, or “percent correct”) about whether children in each age group were able to recognize a word (“targetWord”), the age of the children recognizing the item (“age_group”) and the number of subjects in each age group that we have responses for each item. Please provide a few plots that you think are useful for understanding this dataset. In addition, please plot the proportion of correct responses for certain items by the age of the child responding (choose some subset of the items as there are quite a few). What items show the most variance across age? Please also provide the script you wrote to plot this, in the language of your choice.

## 2. Extracting video descriptives

Use a publicly available machine learning model to extract some information about the short video clip under “question_2”. You can use the audio data, image data, or video data. Document your choice and the outputs from the model, and describe where you see similarities or differences from what is actually happening in the short video. Please demonstrate your ability to use code to do so in some way, even if part of your process uses a a demo version of a package (e.g., on Huggingface).

## 3. Missing files

Your lab mate writes to you with this message.

“My folder on the server (path: /polygon/ucsd/group/vislearnlab/users/XXX) seems to be missing most of my files - I am not sure what happened! The last time I accessed the folder everything looked right. The most recent unusual thing I did, which I am not sure if it is related, is to change permissions for one of my directories using "chmod 777”. Entire subdirectories are cleaned out, rather than random files being corrupted. Sorry for bugging you about this but I need to send out a draft of this paper by the end of the week and I am really worried about what happened!”

Without going into too much detail, describe what could be going on here, and also how you would communicate and work with this person to move forward.

## 4. Project organization

Please describe how you would create and document a research project that includes an online behavioral experiment so that it could be easily understood and reused by a new lab member six months from now.

In your response, include: (1) how you would record and store data both when collecting the data and during analyses, (2) the organizational / folder structure you would implement in your repository, (3) how you would document variable definitions and data transformations, (4) a sample project-level README file, and (5) steps you would take to ensure the project meets standards for reproducibility and public sharing of the data.
