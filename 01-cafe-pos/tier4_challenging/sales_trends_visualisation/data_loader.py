"""
CHALLENGE PART 1 of 3: Load the Data

This project analyses one week of (pretend) real sales data from the
The Trendiest point-of-sale system, stored in weekly_sales.csv. It's split
into 3 files:
    data_loader.py  - (this file) loads the CSV into a usable table
    visualise.py    - turns that table into charts
    main.py         - runs everything and saves the charts as images

weekly_sales.csv has these columns:
    day       - name of the day, e.g. "Monday"
    hour      - the hour of the sale, 24-hour format, e.g. 8 means 8am
    item      - the menu item sold
    quantity  - how many were sold in that single sale
    revenue   - the total $ from that single sale (price * quantity)

YOUR TASK (this file)
----------------------
Use the pandas library to load the CSV file into a DataFrame (think of it
like a spreadsheet you can work with in code).
"""

import pandas as pd
from pathlib import Path


def load_sales(csv_path=Path(__file__).resolve().parent / "weekly_sales.csv"):
    """
    Read csv_path using pandas and return it as a DataFrame.

    Hint:
        return pd.read_csv(csv_path)
    """
    # TODO: implement this function
    return pd.read_csv(csv_path)


if __name__ == "__main__":
    df = load_sales()
    print(df.head())  # show the first 5 rows
    print("\nColumn names:", list(df.columns))
    print("Total rows:", len(df))
