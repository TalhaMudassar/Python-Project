"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

import os
from datetime import date,datetime

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

today = date.today()
now = datetime.now()
time_now = now.strftime("%H:%M:%S")


name = input("Enter your name :").strip()

while True:
    try:
        age = int(input("Enter your age: "))
        break  
    except ValueError:
        print("Please enter age in numbers only!")
        
city = input("Enter your city :").strip()
profession = input("Enter your profession :").strip()
hobby = input("Enter your hobby :").strip()


intro = (
    f"Hello! My name is {name}. I'm {age} years old and live in {city}. "
    f"I work as a {profession} and I absolutely enjoy {hobby} in my free time. "
    "Nice to meet you!"
)

intro += f"\nLogged on: {today} at {time_now}"

border = "*" * (len(intro)-75)

clear_screen()
print("\n" + border)
print(f"*  {intro}  *")
print(border)
