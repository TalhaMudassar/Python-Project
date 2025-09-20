"""
 Challenge: Real-Time Weather Logger (API + CSV)

Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

Your program should:
1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API.
3. Store the following in a CSV file (`weather_log.csv`):
   - Date (auto-filled as today's date)
   - City
   - Temperature (in °C)
   - Weather condition (e.g., Clear, Rain)
4. Prevent duplicate entries for the same city on the same day.
5. Allow users to:
   - Add new weather log
   - View all logs
   - Show average, highest, lowest temperatures, and most frequent condition

Bonus:
- Format the output like a table
- Handle API failures and invalid city names gracefully
"""

import os
import csv
import requests
from datetime import datetime

FILE_NAME = 'weatherlogs.csv'
APIkey = "13e5af3489efc332f4af88cc8c4eec3d"

if not os.path.exists(FILE_NAME):
   with open(FILE_NAME,"w",newline='',encoding='utf-8') as file:
      writer = csv.writer(file)
      writer.writerow(["Date","City","Temprature","Condition"]) 
      
      
def log_weather():
   city = input("Please enter your city name ").strip()
   date = datetime.now().strftime("%Y-%m-%d")
   with open(FILE_NAME,"r",newline='',encoding='utf-8')as file:
      reader = csv.DictReader(file)
      for row in reader:
         if row["Date"] == date and row['City'].lower() == city.lower():
            print("Entry for this data and city already exists")
            
            
   try:
      url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIkey}&units=metric"   
      response = requests.get(url)
      data = response.json()
      
      if response.status_code != 200:
         print(f"API Error {data.get()}")
         return
      temp = data["main"]["temp"]
      condition = data["weather"][0]["main"]
      
      with open(FILE_NAME,'a',newline='',encoding='utf=8')as file:
         writer = csv.writer(file)
         writer.writerow([date,city.title(),temp,condition])
         print(f"Logged: {temp}{condition} in {city.title()} on {date}")
         
   except Exception as e:
      print("FAILED TO MAKE API CALL")
      

def view_logs():
   with open(FILE_NAME,"r",encoding='utf-8')as file :
      reader = list(csv.reader(file))
      if len(reader) <=1:
         print("No new entries")
         return
      for row in reader[1:]:
         print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]}")
      
      
def main():
   while True:
      print("1. Real Time weather logger")
      print("2. Add Weather log")
      
      choice = input("Choose an option: ").strip()
      match choice:     
         case "1": log_weather()
         case "2": view_logs()
         case _: print("Invalid Choice")

         
if __name__ == "__main__":
   main()
            
              
            