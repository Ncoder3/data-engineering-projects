# Mini ETL Pipeline – Cleaning Sales Data in Python

## 📌 Overview
This project demonstrates a basic ETL (Extract, Transform, Load) pipeline using Python and pandas. It processes a mock raw sales dataset, cleans the data, and outputs a cleaned CSV file.

## 🔧 Steps Performed

### 🔹 Extract
- Loaded `raw_sales.csv` containing messy sales data

### 🔹 Transform
- Renamed inconsistent column names
- Handled missing customer names
- Filtered out records with missing or invalid amounts
- Converted date strings to proper `datetime` format

### 🔹 Load
- Saved cleaned dataset as `cleaned_sales.csv`

## 🛠️ Tools Used
- Python
- pandas

## 📁 Files
- `raw_sales.csv`: Original raw input data
- `etl_pipeline.py`: Python script implementing the ETL logic
- `cleaned_sales.csv`: Output file after data cleaning

## 🧠 Learning Outcome
This mini project demonstrates an understanding of real-world data cleaning workflows and a simplified ETL process using Python.
