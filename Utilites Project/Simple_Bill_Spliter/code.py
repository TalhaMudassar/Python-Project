"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""


def get_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("❌ please enter a valid number")
        

number_people = int(input("How man people are in the group "))
names = []
for i in range(number_people):
    name = input(f"Enter name of the person {i+1} :")
    names.append(name)
    
total_bill = get_float("Enter the bill amount in number's only ")

share = round(total_bill / number_people , 2)

print("\n" + "*" * 40)
print(f"Total bill: {total_bill}")
print(f"Each Person owns {share}")


for name in names:
    print(f"{name} owns {share} rupees ")
    
    
print("\n" + "*" * 40)