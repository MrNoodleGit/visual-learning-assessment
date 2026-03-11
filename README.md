# Visual Learning Lab Assessment (Ra Mour, March 2026)

## Overview

Submission for Ra Mour's assessment to join the Visual Learning Lab.

Please see the assessment folder for my written responses to each part. Also, view `notebooks/q1-plots.ipynb` to find my plots for part 1.

`data-output/output_clip_faces.mp4` is a version of the example clip with bounding boxes that track the faces in each frame, produced using the RetinaFace computer vision library and OpenCV.

`data-output/gemini-video-captions/gemini_video_caption_1.txt` is a sample video caption using the Gemini API.

## Repository Structure

```
.
├── assessment # written responses to the assessment
│   ├── 0_questions.md
│   ├── 1_visualization.md
│   ├── 2_video_descriptives.md
│   ├── 3_missing_files.md
│   ├── 4_project_organization.md
│   └── 4_sample_README.md
├── data-output # output of video caption and face detection models
│   ├── gemini-video-captions
│   ├── output_clip_faces.mp4
│   └── qwen3-video-captions
├── environment.yml # conda dependencies
├── notebooks # plots for part 1: visualization
│   └── q1-plots.ipynb
├── README-Template.md
├── README.md
├── scripts # scripts for part 2: video descriptives
│   ├── gemini-object-detection.py
│   ├── gemini-video-caption.py
│   ├── qwen-video-caption.py
│   └── retina_video_face_detection.py
└── task-data # original data from the assessment instructions
    ├── q1_visualizing_data
    └── q2_videodescriptives

10 directories, 15 files
```

## Requirements

- Python 3.14.3
- Conda
- Pandas
- Seaborn
- Tensorflow

Please see the environment.yml file for the full list of dependencies.

## Setup

```bash
# Clone the repository
git clone https://github.com/MrNoodleGit/visual-learning-assessment/tree/main
cd visual-learning-assessment

# Create and activate the conda environment
conda env create -f environment.yml
conda activate visual-learning
```

The retina_video_face_detection.py must be run on a GPU server (e.g. Google Colab with T4 GPU).

## Contact

[Ra Mour](https://ramour.org/)

## AI USE DISCLAIMER

For most of this assessment, I made about 20% use of AI tools--primarily as a search mechanism to explore online resources and code documentation or to get simple code advice (e.g. group pandas dataframe manipulation). My aim was to somewhat replicate how I would work before the breakthrough of AI programming. This was both to highlight my own baseline thinking and working process and make sure I had a direct understanding of how I produced each portion of my work as I progressed.

For part 4: Project Organization, I used Claude to help generate a plausible folder structure and sample README, which I then modified for my specific use.
