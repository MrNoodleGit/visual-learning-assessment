# Vocabulary Acquisition Study

## Overview

This project investigates which words are easier or more difficult for children to understand. We examine how children aged 3 to 11 can recognize certain words (e.g., “apple”) in the presence of a distractor image (e.g., “carrot”). The data were collected via an online behavioral
experiment.

## Repository Structure

- `experiment/` — task code
- `data/raw/` — unmodified (export from Databrary before running analyses)
- `data/processed/` — cleaned data produced by `analysis/01_data_cleaning.py`
- `analysis/` — Python scripts; run in numbered order
- `notebooks/` — exploratory Jupyter notebooks (not part of main pipeline)
- `docs/` — IRB approval, preregistration, task description

## Requirements

- Python 3.14.3
- Conda
- Pandas
- Seaborn

## Setup

```bash
# Clone the repository
git clone https://github.com/MrNoodleGit/visual-learning-assessment/tree/main
cd visual-learning-assessment

# Create and activate the conda environment
conda env create -f environment.yml
conda activate visual-learning
```

## How to Reproduce

Run scripts in order from the project root:

```bash
python analysis/01_data_cleaning.py
python analysis/02_descriptives.py
python analysis/03_main_analyses.py
```

Figures will be saved to `analysis/figures/`.

## Data

- Raw data: https://www.databrary.org/volume/1882
- Sensitive details were removed prior to sharing
- Preregistration: https://osf.io/kwvxu/overview
- Ethics approval: IRB

## Contact

Ra Mour, Visual Learning Lab, ramour@ucsd.edu — last updated March 11, 2026
