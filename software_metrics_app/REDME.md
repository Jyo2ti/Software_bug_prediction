Redme file: # Software Metrics and Bug Prediction

This Streamlit app provides insights into software metrics and offers bug prediction functionality based on these metrics.

## Setup

1. Clone this repository:
   
   git clone <repository-url>
   cd software_metrics_app
   

2. Create a virtual environment and activate it:
   
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   

3. Install the required packages:
   
   pip install -r requirements.txt
   

## Running the App

To run the Streamlit app, use the following command:


streamlit run app.py


This will start the app and open it in your default web browser.

## Features

- Display information about various software metrics
- Predict the likelihood of bugs based on input metrics
- Show feature importances for bug prediction
- Display sample data and basic statistics from the dataset
- Visualize correlation between different metrics

## Project Structure


software_metrics_app/
│
├── data/
│   └── software_metrics_data.csv
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── model.py
│   └── utils.py
│
├── app.py
├── requirements.txt
└── README.md


- data/: Contains the dataset used for analysis and prediction
- src/: Contains the source code for data loading, model training, and utility functions
- app.py: The main Streamlit application file
- requirements.txt: List of Python packages required for the project
- README.md: This file, containing project information and setup instructions