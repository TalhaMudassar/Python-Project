"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""


def calculator_minute(age_years):
    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAYS = 24
    MINUTE_IN_HOUR = 60
    SECOND_IN_MINUTE = 60
    
    total_days = DAYS_IN_YEAR * age_years
    total_hours = total_days * HOURS_IN_DAYS
    total_minutes = total_hours * MINUTE_IN_HOUR
    total_seconds = total_minutes * SECOND_IN_MINUTE
    
    return round(total_days), round(total_hours), round(total_minutes),round(total_seconds)


while True:
    try:
        age = float(input("Enter age: "))
        days,hours,minutes,seconds = calculator_minute(age)
        print("\nYou are approximately: ")
        print(f"DAYS: {days:,}")
        print(f"HOURS: {hours:,}")
        print(f"MINUTES: {minutes:,}")
        print(f"SECONDS: {seconds:,}")
        
        again = input("if you want to continue (y/n)")
        if again != "y":
            print("CODE COMPLETE ☺")
            break
    except:
        print("Please enter a valid number of age ")
        
    
