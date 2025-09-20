"""
Sample data:
Date,City,Temperature,Condition
2025-06-11,Delhi,36.5,Clear
2025-06-12,Delhi,37.8,Sunny
2025-06-13,Delhi,38.0,Sunny
2025-06-14,Delhi,34.2,Rain
2025-06-15,Delhi,35.0,Clouds
2025-06-16,Delhi,33.4,Rain
2025-06-17,Delhi,34.7,Clear

Plot graphs from this data
"""

import csv
from collections import defaultdict
import matplotlib.pyplot as plt


def visualize_weather():
    dates = []
    temps = []
    conditions = defaultdict(int)  # we get all value in integer by using this
    
    with open(FILENAME,'r',encoding='utf-8')as file:
        reader =csv.DictReader(file)
        for row in reader:
            try:
                dates.append(row['Date'])
                temps.append(row['Temprature'])
                conditions[row["Condition"]] += 1 
            except:
                continue
            
    if not dates:
        print("No data available")
        return
    
    plt.figure(figsize=(10,7))
    plt.plot(dates,temps)

FILENAME = 'weatherlogs.csv'
