"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time
import sys
import platform


def beep():

    if platform.system() == "Windows":
        try:
            import winsound
            winsound.Beep(1000, 500)  
            return
        except Exception:
            pass
    # Fallback: BEL character (may or may not produce sound)
    print('\a', end='', flush=True)
    

def long_beep():
    """Long beep for 5 seconds"""
    if platform.system() == "Windows":
        try:
            import winsound
            winsound.Beep(1000, 5000)
            return
        except Exception:
            pass
   
    for _ in range(5):
        print('\a', end='', flush=True)
        time.sleep(1)
    

while True:
    try:
        seconds = int(input("Enter the time in second"))
        if seconds < 1:
            print("Please enter a number greater than 0")
            continue
        break 
    except ValueError:
        print("invalid input please enter a whole number")
    except KeyboardInterrupt:
        print("\nInput cancelled.")
        raise SystemExit
        
        
        
print("\n🔔 Timer Started ...")  
try:
    for remaining in range(seconds,0,-1):
        mins,secs = divmod(remaining,60)
        time_format = f"{mins:02} : {secs:02}"
        print(f"⌛ Time left: {time_format}", end='\r', flush=True)
        time.sleep(1)
        beep()
    print("\n Time's up ")
    long_beep()
except KeyboardInterrupt:
    print("\n Tme's up! Take a break or move to the next task ")

        
        