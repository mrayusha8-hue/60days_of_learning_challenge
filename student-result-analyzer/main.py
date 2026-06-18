students = []   # list to store student records
total_marks = 100

#-----calculate_grade function------
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    else:
        return "Fail" 
    
def statistic_function():
    if len(students) == 0:
        print("No student records found!")
        return 
    
    total_students = len(students)
    pass_count = 0
    fail_count = 0
    total_marks = 0

    for student in students:
        total_marks += student["marks"]

        if student["grade"] == "Fail":
            fail_count += 1
        else:
            pass_count += 1

    average = total_marks / total_students
    print("\n--- Statistics ---")
    print("Total Students:", total_students)
    print("Passed:", pass_count)
    print("Failed:", fail_count)
    print("Average Marks:", average)
     
#-----Add Function-----
def add_student():
   num = int(input("How many students to add: "))
   for i in range(num):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    percentage = (marks / total_marks) * 100   # calculate percentage
    grade = calculate_grade(percentage)
    
    student = {
        "name": name,
        "marks": marks,
        "percentage": percentage,
        "grade": grade
    }
    students.append(student)
    print("Student records added successfully!")
  
#------View Function------
def view_student():
    if len(students) == 0:
        print("No student records found!")
        return

    print("\n---Students Record---")
    for student in students:
            print(f"{'Name':<12} : {student['name']}")
            print(f"{'Marks':<12} : {student['marks']}")
            print(f"{'Percentage':<12} : {student['percentage']:.2f}%")
            print(f"{'Grade':<12} : {student['grade']}")
            print("-----------------------")

#-----Topper_Function---------          
def find_topper():  
    if len(students) == 0:
        print("No student records found!")
        return
    # Filter out failing students
    passed_students = [s for s in students if s["grade"] != "Fail"]

    if passed_students:
        # Find the highest marks among passed students
        highest_marks = max(s["marks"] for s in passed_students)

        # Collect all students who have those highest marks
        toppers = [s for s in passed_students if s["marks"] == highest_marks]

        print("\nTopper(s):")
        for topper in toppers:
         print(f"{'Name':<12} : {topper['name']}")
         print(f"{'Marks':<12} : {topper['marks']}")
         print(f"{'Percentage':<12} : {topper['percentage']:.2f}%")
         print(f"{'Grade':<12} : {topper['grade']}")
         print("-----------------------")
    else:
        print("\nNo topper found (all students failed).")

#------Search funtion--------

def search_student():
    search_name = input("\nEnter student name to search: ").lower()
    found = False
    for student in students:
     if student["name"].lower() == search_name.lower():
       print(f"{'Name':<12} : {student['name']}")
       print(f"{'Marks':<12} : {student['marks']}")
       print(f"{'Percentage':<12} : {student['percentage']:.2f}%")
       print(f"{'Grade':<12} : {student['grade']}")
       found =  True
       break
    if found == False:
     print("Student not found")



#-----MENU-----
while True:
    print("\n===== Student Result Analyzer =====")
    print("1. Add Students")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Statistics")
    print("6. Exit")

    choice = input("\nEnter choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
      find_topper()
    elif choice == "5":
      statistic_function()
    elif choice == "6":
        print("Exited")
        break
    else:
        print("Invalid choice, try again")





