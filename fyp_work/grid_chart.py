import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Monthly summarized project phases with shorter descriptions
monthly_data = [
    ["Oct 2025", "Requirements & Design"],
    ["Nov 2025", "Data & Model Training"],
    ["Dec 2025", "Model Evaluation & Testing"],
    ["Jan 2026", "App UI Development"],
    ["Feb 2026", "Database & Integration"],
    ["Mar 2026", "Full System Testing"],
    ["Apr 2026", "Documentation & Review"],
    ["May 2026", "Final Presentation"]
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

# Plot simplified Gantt chart
plt.figure(figsize=(10, 6))

# Iterate using iterrows to safely handle column names
for index, row in df_month.iterrows():
    plt.barh(row['Phase Summary'], (row['End'] - row['Start']).days, left=row['Start'], color="skyblue", edgecolor="steelblue", height=0.6)

plt.xlabel("Timeline", fontsize=12)
plt.ylabel("Project Phases", fontsize=12)
plt.title("Project Schedule Overview (Grid Style)", fontsize=16, weight="bold")

# Reverse the y-axis for chronological order from top
plt.gca().invert_yaxis()

# --- Changes for square box grid ---
# Set both x and y grid to True and adjust linestyle and alpha for visibility
plt.grid(True, axis='both', linestyle=':', alpha=0.7, color='gray') # Changed to dotted lines for a subtle grid

# Set major locators for the y-axis to create horizontal grid lines for each phase
plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True)) # Ensures a tick for each phase
# --- End changes ---

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the new chart
output_path = "Gantt_Chart_With_Square_Grid.png"
plt.savefig(output_path, dpi=300)
print(output_path)