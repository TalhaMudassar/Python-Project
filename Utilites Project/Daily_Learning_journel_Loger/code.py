"""
 Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""
import datetime

entry = input("Ask the user what they learned today").strip()
rating = input("  ⭐Rating your prodctivity today(1-5),optional").strip()

now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d - %I:%M %p")

journel_entry = f"\n 📅 {date_str} \n {entry} "
if rating:
    journel_entry += f" \n Productivity Rating: {rating} "   
journel_entry += "\n" + "-" * 50

with open("input.txt","a",encoding="utf8") as f:
    f.write(journel_entry)
    
print(f"\n your journal entry has been saved to 'learning_journal.txt' file. ")
    
