"""
 Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""

# def userdata():
#     students = []
#     while True:
#         names = input("Enter your name ,(exit) for exit ").strip()
#         if names.lower() == "exit":
#             break
        
#         if any(s['name'].lower() == names.lower() for s in students):   
#             print(" Duplicate name! Please enter a different student name.")
#             continue
#         try:
#             marks = int(input("Enter marks {names}"))
#         except ValueError:
#             print(" invalid input make should be integer ")  
#             continue
        
#         students.append({'name':names,'marks':marks})
#     return students


# def print_display(students):
#     marks_list = []
#     if not students:
#         print("No Student Data Available")
#         return

#     marks_list = [s['marks'] for s in students]
#     average_mark = sum(marks_list) / len(students)
#     max_mark = max(marks_list)
#     min_mark = min(marks_list)
    
#     for s in students:
#         if max_mark == s['marks']: 
#             highest_student = s['name']
#         elif min_mark == s['marks']:
#             lowest_student = s['name']
#         # collect all top and bottom scorers
#     highest_students = [s['name'] for s in students if s['marks'] == max_mark]
#     lowest_students = [s['name'] for s in students if s['marks'] == min_mark]
    
        
#     print("\n ---- Student Marks Report ---- ")
#     print(f"Total Students: {len(students)}")
#     print(f"Average Marks: {average_mark:.2f}")
#     print(f"Highest Marks: {max_mark} by {', '.join(highest_students)}")
#     print(f"Lowest Marks: {min_mark} by {', '.join(lowest_students)}")
#     print("-----------------------------------")
    
          
# def main():
#     Stu_dat = []
#     while True:
#         print("Enter 1 for  make student record")
#         print("Enter 2 for displaying the data")
#         print("Enter 3 for exit the program")
        
#         choice = int(input("Enter choice"))
     
#         if choice == 1:
#             Students_data = userdata()
            
#             print("\n COMPLETE DATA")
#             for s in Students_data:
#                 Stu_dat.append(s)
#                 print(f" Name{s['name']} - Numbers {s['marks']}")
#         elif choice == 2:
#             print_display(Stu_dat)
        
#         elif choice == 3:
#             print("GOOD BYR ")
#             break
#         elif _:
#             print("PLEASE ENTER A VALID INPUT")
        
# main()


#bu using dictionary

def collect_student_data():
    students = {}
    while True:
        name = input("Enter the student name ").strip()
        if name.lower() == "done":
            break
        if name in students:
            print(" Student already exists ")
            continue
        
        try:
            marks = float(input("Enter marks for {name} "))
            students[name] = marks
        except ValueError:
            print("Please enter a valid number for marks ")
    return students

def display_report(students):
    if not students:
        print("No student data ❌")
        return
    
    marks = list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    average = sum(marks) / len(marks)

    topper = [name for name, score in students.items() if score == max_score ]
    bottomer = [name for name, score in students.items() if score == min_score ]

    print("\n Students marks report 🗓️")
    print("-" * 30)
    print(f"Total students: {len(students)}")
    print(f"average marks for students: {average:.2f}")
    print(f"Highest marks : {max_score} by {', '.join(topper)}")
    print(f"lowest marks : {min_score} by {', '.join(bottomer)}")

    print("-" * 30)
    print("Detailed Marks 🗓️")
    for name, score in students.items():
        print(f" - {name}: {score}")


students = collect_student_data()
display_report(students)