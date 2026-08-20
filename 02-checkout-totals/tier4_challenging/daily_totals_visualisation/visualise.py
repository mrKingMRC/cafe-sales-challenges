"""
CHALLENGE PART 2 of 3: Chart the Data

Complete data_loader.py first. This file turns the daily totals DataFrame
into two charts using matplotlib.

YOUR TASK (this file)
----------------------
Implement both functions below. Each one should build a chart using
matplotlib and matplotlib's `savefig` should NOT be called here — that
happens in main.py. Just build the chart with plt (it will be shown or
saved by whoever calls these functions).

BONUS IDEA (optional, no TODO required): once both charts below are
working, try adding a 7-day rolling/moving average line on top of the
daily revenue chart, using df["total_sales"].rolling(7).mean() — this
smooths out day-to-day noise so trends are easier to see.
"""

import matplotlib.pyplot as plt


def plot_daily_revenue(df):
    """
    Create a line chart showing total_sales for the most recent 30 days
    in df, in date order, so the café can see how revenue moved across
    that month.

    Steps:
      1. Sort df by "date" (ascending) and take the LAST 30 rows
         (the most recent month) — e.g. df.sort_values("date").tail(30)
      2. Plot "date" on the x-axis and "total_sales" on the y-axis as a
         line chart (plt.plot(...)).
      3. Add a title ("The Trendiest — Daily Revenue (Last 30 Days)"), and
         axis labels ("Date", "Total Sales ($)").
      4. Rotate the x-axis labels 45 degrees so they don't overlap:
         plt.xticks(rotation=45, ha="right")
      5. Call plt.tight_layout() so nothing gets cut off.
    """
    df.sort_values("date").tail(30)
    
    fig, ax = plt.subplots()

    ax.bar(df["date"], df["total_sales"], 0.5, label='Online', color='teal')

    # Fix X-axis labels over the adjusted groups
    #ax.set_xticks(x)
    #ax.set_xticklabels(categories)

    plt.title("The Trendiest — Daily Revenue (Last 30 Days)")
    plt.xlabel('Date')
    plt.ylabel('Total Sales ($)') 
    plt.xticks(rotation=45,ha="right")
    plt.tight_layout()


def plot_average_by_day_of_week(df):
    """
    Create a bar chart showing the AVERAGE total_sales for each day of
    the week (across the whole dataset), so the café can see which days
    are busiest.

    Steps:
      1. Group df by "day_of_week" and take the mean of "total_sales".
      2. Reorder the result so days appear Monday through Sunday (not
         alphabetically!). Hint:
             day_order = ["Monday", "Tuesday", "Wednesday", "Thursday",
                           "Friday", "Saturday", "Sunday"]
             averages = df.groupby("day_of_week")["total_sales"].mean()
             averages = averages.reindex(day_order)
      3. Plot it as a bar chart (plt.bar(...)) with days on the x-axis
         and average revenue on the y-axis.
      4. Add a title ("The Trendiest — Average Revenue by Day of Week"),
         and axis labels ("Day of Week", "Average Total Sales ($)").
      5. Rotate the x-axis labels 45 degrees: plt.xticks(rotation=45, ha="right")
      6. Call plt.tight_layout().
    """
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
    averages = df.groupby("day_of_week")["total_sales"].mean()
    averages = averages.reindex(day_order)

    rolling = df["total_sales"].rolling(7).mean()
    rolling = rolling.reindex(day_order)
    
    fig, ax = plt.subplots()

    ax.bar(day_order, averages, 0.5, label='Online', color='teal')
    

    plt.title("The Trendiest — Average Revenue by Day of Week")
    plt.xlabel("Day of Week")
    plt.ylabel("Average Total Sales ($)") 
    plt.xticks(rotation=45,ha="right")
    plt.legend()
    plt.tight_layout()