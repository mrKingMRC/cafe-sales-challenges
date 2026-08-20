"""
CHALLENGE PART 1 of 3: Load the Data

This project analyses several months of (pretend) daily checkout totals
from the The Trendiest till, stored in daily_totals.csv. It's split into
3 files:
    data_loader.py  - (this file) loads the CSV into a usable table
    visualise.py    - turns that table into charts
    main.py         - runs everything and saves the charts as images

daily_totals.csv has these columns:
    date                       - the date, e.g. "2026-01-01"
    day_of_week                - name of the day, e.g. "Monday"
    total_sales                - total $ taken at the till that day
    num_transactions           - how many separate sales happened that day
    average_transaction_value  - total_sales / num_transactions for that day

YOUR TASK (this file)
----------------------
Use the pandas library to load the CSV file into a DataFrame (think of it
like a spreadsheet you can work with in code), making sure the "date"
column is parsed as an actual date (not just text).
"""

import pandas as pd
from pathlib import Path


def load_daily_totals(csv_path=Path(__file__).parent / "daily_totals.csv"):
    """
    Read csv_path using pandas and return it as a DataFrame, with the
    "date" column parsed as a real date type.

    Hint:
        return pd.read_csv(csv_path, parse_dates=["date"])
    """
    return pd.read_csv(csv_path, parse_dates=["date"])


if __name__ == "__main__":
    df = load_daily_totals()
    print(df.head())  # show the first 5 rows
    print("\nColumn names:", list(df.columns))
    print("Total rows:", len(df))
