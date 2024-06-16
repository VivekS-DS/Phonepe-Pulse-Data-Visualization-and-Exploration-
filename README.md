# Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly

# PhonePe Pulse Data Visualization Capstone Project

## Project Overview

This capstone project aims to develop a comprehensive solution for extracting, transforming, storing, and visualizing data from the PhonePe Pulse GitHub repository. The objective is to create a live geo-visualization dashboard that presents valuable insights and statistics in an interactive and user-friendly manner.

## Problem Statement

The PhonePe Pulse GitHub repository contains extensive data related to various metrics and statistics. The goal is to process this data to derive insights that can be effectively visualized. The solution involves the following steps:

1. Extract data from the PhonePe Pulse GitHub repository using scripting.
2. Transform the data into a suitable format and perform necessary cleaning and pre-processing.
3. Store the transformed data in a MySQL database for efficient retrieval.
4. Develop a live geo-visualization dashboard using Streamlit and Plotly in Python.
5. Provide at least 10 different dropdown options for users to explore various facts and figures on the dashboard.

## Solution Approach

### Step 1: Data Extraction

- Clone the PhonePe Pulse GitHub repository using scripting.
- Store the extracted data in formats such as CSV or JSON for further processing.

### Step 2: Data Transformation

- Use Python and libraries like Pandas to clean and preprocess the data.
- Handle missing values and transform the data into a format suitable for analysis and visualization.

### Step 3: Database Insertion

- Utilize the `mysql-connector-python` library to connect to a MySQL database.
- Insert the transformed data into the database using SQL commands.

### Step 4: Dashboard Creation

- Develop an interactive dashboard using Streamlit and Plotly libraries in Python.
- Use Plotly's geo map functions to display data on a map.
- Incorporate multiple dropdown options in Streamlit for users to select different facts and figures to display.

### Step 5: Deployment

- Ensure the solution is secure, efficient, and user-friendly.
- Thoroughly test the solution and deploy the dashboard publicly for user access.

## Results

The final deliverable will be a live geo-visualization dashboard that:
- Displays insights and statistics from the PhonePe Pulse GitHub repository interactively.
- Provides at least 10 different dropdown options for exploring various metrics.
- Ensures efficient data retrieval through a MySQL database.
- Is accessible from a web browser, allowing easy navigation and exploration of data.

## Repository Structure

```plaintext
.
├── data
│   ├── processed & transformed
├── scripts
│   ├── phonepe_app.py
│   ├── phonepe_data_extraction.ipynb
├── requirements.txt
├── README.md
└── LICENSE
```

## Getting Started

### Prerequisites

- Python 3.12+
- MySQL Database
- Git

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/PhonePe/pulse.git
   cd phonepe-pulse-data-visualization
   ```

2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   ```sql
   CREATE DATABASE phonepe_pulse;
   ```

### Running the Scripts

4. **Run the Dashboard:**
   ```sh
   streamlit run phonepe_app.py
   ```

## Usage

- Access the dashboard via your web browser at the local host address provided by Streamlit.
- Use the dropdown options to explore various insights and statistics from the PhonePe Pulse data.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PhonePe Pulse](https://github.com/PhonePe/pulse) for providing the data.
- Contributors and the open-source community for their valuable tools and libraries.


