import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Monthly summarized project phases
monthly_data = [
    ["Oct 2025", "Requirement Gathering, System Design, Dataset Collection & Cleaning"],
    ["Nov 2025", "Data Labeling, Model Setup & Initial Training"],
    ["Dec 2025", "Model Evaluation, Improvement, Optimization & Testing"],
    ["Jan 2026", "App Planning, Setup, UI Development & Testing"],
    ["Feb 2026", "Database, Nutrient & Price Modules, Model Integration"],
    ["Mar 2026", "Integration Testing, Optimization, Feature Refinement, Internal Testing, Bug Fixing"],
    ["Apr 2026", "Documentation, Testing Summary & Report Review"],
    ["May 2026", "Presentation Prep, Demo, Advisor Review & Final Submission"]
]

# Convert to DataFrame
df_month = pd.DataFrame(monthly_data, columns=["Month", "Phase Summary"])

# Define start and end dates for each month
month_starts = {
    "Oct 2025": ("2025-10-01", "2025-10-31"),
    "Nov 2025": ("2025-11-01", "2025-11-30"),
    "Dec 2025": ("2025-12-01", "2025-12-31"),
    "Jan 2026": ("2026-01-01", "2026-01-31"),
    "Feb 2026": ("2026-02-01", "2026-02-28"),
    "Mar 2026": ("2026-03-01", "2026-03-31"),
    "Apr 2026": ("2026-04-01", "2026-04-30"),
    "May 2026": ("2026-05-01", "2026-05-31")
}

df_month["Start"] = [datetime.strptime(month_starts[m][0], "%Y-%m-%d") for m in df_month["Month"]]
df_month["End"] = [datetime.strptime(month_starts[m][1], "%Y-%m-%d") for m in df_month["Month"]]

# Plot simplified Gantt chart (monthly)
plt.figure(figsize=(10, 6))
for i, row in enumerate(df_month.itertuples(), 1):
    plt.barh(row.Month, (row.End - row.Start).days, left=row.Start, color="skyblue", edgecolor="black")

plt.xlabel("Timeline", fontsize=12)
plt.ylabel("Months", fontsize=12)
plt.title("Simplified Project Schedule (Monthly Gantt Chart)", fontsize=15, weight="bold")
plt.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.tight_layout()

# Save the new chart
output_path = "Simplified_Monthly_Gantt_Chart.png"
plt.savefig(output_path, dpi=300)
output_path
