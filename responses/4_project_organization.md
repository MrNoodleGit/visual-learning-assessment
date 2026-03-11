4.

# Project Organization

## During Data Collection

I would:

- store raw data on a secure academic server. I'd keep it in a dedicated data/raw/ folder and set it to read-only.
- use a consistent, machine-readable naming convention for files.
- make sure to store a data dictionary alongside the raw data at the time of collection (to avoid forgetting the meaning of variables and how they were derived later on).

## During Data Analysis:

- I'd ensure that processed data follows a clear chain. Every transformation should be scripted, not done by hand to maintain reproducibility and understand the progression of how data was produced.

- Transformed data should be kept seperate from raw data. Raw data must never be modified directly.

- I'd make sure to use relative paths in scripts, not absolute paths that would cause the code to break if someone runs it on a different system.

## 2. Folder Structure

```
project-root/
│
├── README.md
├── .gitignore
├── environment.yml # Conda environment
│
├── experiment/ # Online experiment code
│ ├── index.html
│ ├── psychopy/
│ └── stimuli/
│
├── data/
│ ├── raw/ # download from databrary (do not modify directly)
│ ├── processed/ # Output of cleaning scripts
│ └── codebook.md
│
├── analysis/
│ ├── 01_data_cleaning.py
│ ├── 02_descriptives.py
│ ├── 03_main_analyses.py
│ └── figures/
│
├── notebooks/ # exploratory Jupyter notebooks
│ └── plots.ipynb
│
├── docs/
│ ├── preregistration.md
│ ├── IRB_approval.pdf
│ └── task_description.md
│
└── outputs/
├── manuscript/
└── supplementary/
```

## Data Documentation

I would include the following in a data dictionary (data/codebook.md in example folder structure below)

- Variable name
- Variable type (string, integer, float)
- possible range of values
- Units
- An explanation of the data, how it was derived, and the default value for missing data (e.g. NONE)

## Reproducibility & Public Sharing

- Dependency management: I use conda to maintain code environments in Python
- Set a random seed in any script with randomness to obtain similar results in other runs of the project
- Run everything via scripts
- Only use relative paths throughout all code
- Git and GitHub for version control throughout the entirety of the project

### Before Public Sharing

- Remove any details that could identify participants
- Preregister the hypotheses and analysis plan on OSF before data collection
- Choose a license: For example, CC BY 4.0 for data and MIT for code. This determines how other people can use your project in the future.
- FAIR principles: Ensure data is Findable, Accessible, Interoperable, and Reusable

Sources:

https://experimentology.io/

https://www.go-fair.org/fair-principles/
