"""

 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added

"""

# fist run in terminal pip install pip 
# if already install than run pip install --upgrate pip 
# than run : pip install csv


import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
   with open(FILENAME,'w',encoding='utf-8') as file:
     writer = csv.writer(file)
     writer.writerow(["Name","phone","Email"]) 
     
     
     
def add_contact():
   name = input("Enter the name ").strip()
   phone = input("Enter phone number")
   email = input("Enter your email")
   
   
   # check the duplication
   with open(FILENAME,'r',encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
         if row["name"].lower() == name.lower():
            print("Contact Name already exists")
            return
         
   with open(FILENAME,'a',encoding='utf-8') as file:
      writer = csv.writer(file)
      writer.writerow([name,phone,email])
      print("Contact Added")
      
def view_contact():
   with open(FILENAME,'r',encoding='utf-8')as file:
      reader = csv.reader(file)
      rows = list(reader)
      if len(rows) < 1:
         print("No contacts ")
         return
      print("\nYOUR CONTACTS\n")
      for row in rows[1:]:
         if len(row) < 3:   # avoid IndexError
             continue
         print(f"{row[0]} | {row[1]} | {row[2]}")
      print()
         
         
def search_contact():
   name = input("Enter name for searching").strip()
   found = False
   with open(FILENAME,'r',encoding='utf-8')as file:
      readers = csv.DictReader(file)
      for row in readers: 
         if name in row['Name'].lower():
            print(f"{row["Name"]} | {row["phone"]}")
            found = True
            
   if not found:
      print("No Matching contact found")
            
            
def main():
   while True:
      try:
         print("\n Contact Book")
         print("press1. Add Contact")
         print("press2. View All contacts")
         print("press3. search contacts")
         print("press4. Exit Program")
         choice = int(input("please enter you choose b/w 1-4"))
         if choice == 1:
            add_contact()
         elif choice == 2:
            view_contact()
         elif choice == 3:
            search_contact()
         elif choice == 4:
            print("Thanks for using our system")
            break
         else:
            print("Please enter a correct choice")
            
            
      except ValueError:
         print("Error occurs")
         
         
main()
         
   # if readers['name'] == name 
   # for row in rows[1:]:
   #    if row[0] == name:
   #       found = True
            
       
