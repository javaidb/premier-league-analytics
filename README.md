

<p align="center">
  <img src="https://github.com/user-attachments/assets/fb9e25ea-77d0-484e-a37d-7ecbc4e6d6ed" alt="Fantasy Logo" width="150" />
</p>

# Performance Analysis for Fantasy Premier League (FPL)

This project is used a personal self-study into several areas such as data collection & wrangling, feature engineering, data analysis & modeling and visualization. At surface level, it is used as a broad view of in-form players currently in the Premier League to inform an ideal Fantasy Premier League (FPL) team to maximize performance/points output. FPL is a game which assigns points to a player based on their performance output in a given game week, and so, being able to assess performance over time either by modeling or by assessment of surface statistics is vital to maximize returns.

## Project Structure

This project is organized into several directories, each serving a specific purpose:
```
    fpl-analytics/
    ├── notebooks/           # Jupyter notebooks for interactive exploration
    │   └── visualize_metrics_fpl.ipynb  # Main notebook for testing and visualization of FPL data
    │   └── visualize_metrics_understat.ipynb  # Main notebook for testing and visualization of Understat darta + FPL
    ├── src/                 # Destination for source code of various modules
    │   └── config/          # Initialization to cater to personal user
    │   │   └── config.py      # Settings regarding color schemes
    │   │   └── data_template.json      # Settings regarding personal FPL information to extract from (Need to rename as data.json once cloned)
    │   └── functions/       # Modules and associated functions by which API data is extracted, consolidated and analyzed
    │   │   └── raw_data_fetcher.py      # Module for fetching raw data from APIs and assigning to variables
    │   │   └── data_builder.py      # Module for building relations ahd consolidations of and between raw data
    │   │   └── generated_helper_fns.py      # Module for extracting helper functions from newly fetched/constructed datasets, for use later on
    │   │   └── data_analysis.py      # Module for interpreting and transforming data for actionable insights
    │   │   └── data_visualization.py      # Module for any and all data visualization
    │   │   └── data_exporter.py      # Module for exporting data to proper formats
    │   │   └── helper_utils.py      # Standalone module for general helper utility functions
    │   │   └── notebook_utils.py      # Standalone module for general notebook utility functions
    ├── tests/               # Sample unit testing modules
    ├── README.md            # Project overview and documentation
    └── requirements.txt     # List of dependencies required to run the project
```

## Getting Started


To run this project, you will need Python installed on your machine along with the required libraries. Current version utilizations being utilzied locally are as follows:
- Python (3.11.7)
- Virtual environment created using Python 3.11 (Not required but suggested)

To create and activate virtual environment:

```bash
python -m venv .venv_fpl
source .venv_fpl/bin/activate  # Linux/Mac
# or
.venv_fpl\Scripts\activate  # Windows

ipython kernel install --user --name=".venv_fpl" --display-name="FPL Analytics"
```

Otherwise, this repo primarily works by processing data from various APIs and consolidating it through various modules and visualized via jupyter notebooks. General setup is as follows:

- Clone this repository to your local machine.
- Within src/config, rename data_template.json -> data.json.
- Make the following adjustments to data.json:
   - "beacon_team_ids" - a custom feature to include rival IDs you would like to measure your team against, typically those with demonstrated success.
   - "personal_team_id: - entry to include your personal FPL team ID (use link [here](https://fpl.team/find-id/) to see how to find your FPL ID).
   - "personal_league_ids" - used to track statistics and ranks within leagues your FPL team belongs to (or whichever is entered within "personal_team_id").
- Navigate to notebooks folder and open "visualize_metrics" within jupyter environment. Visualization and consolidation of FPL details are implemented through here.
- To execute, simply hit run all.

## Acknowledgements

 - [Fantasy Premier League](https://fantasy.premierleague.com/)
 - [Understat](https://understat.com/)

<p align="center">
  <img src="https://github.com/user-attachments/assets/fb9e25ea-77d0-484e-a37d-7ecbc4e6d6ed" alt="Fantasy Logo" width="150" />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/5a84e55c-e687-4c93-95f7-800398b3b46d" alt="PL Logo" width="140" />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/99f5727b-1ff8-48e9-861d-534775dddce8" alt="GH Logo" width="50" />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/ba805d10-6560-4c61-a4f6-ccccf46dd5ba" alt="SKLearn Logo" width="120" />
</p>

## Authors

- [@javaidb](https://www.github.com/javaidb)

## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![IBM License](https://img.shields.io/badge/Certificate_ML-IBM-green.svg)](https://www.credly.com/badges/6d82b78c-cade-4a4c-94cb-b7f89e142350/public_url)
