students = []   # list to store student records

total_marks = 100

while True:
    name = input("Enter student_name (q to quit): ")
    if name.lower() == 'q':
        break
    else:
        marks = int(input("Enter marks: "))
        percentage = (marks / total_marks) * 100   # calculate percentage

        student = {
            "name": name,
            "marks": marks,
            "percentage": percentage
        }
        students.append(student)

# print all students after loop ends
print("\n--- Student Records ---")
for s in students:
    print(f"Name: {s['name']}, Marks: {s['marks']}, Percentage: {s['percentage']:.2f}%")

#def add_student():
 #   students = []
'''std1={
    "name" :"Ram Dahal",
        "marks": subjects,
        "percentage": percentage,
        "grade": grade

#}'''

'''while True:
 name = input("Enter student_name(q to quit):")
 if name=='q':
  break
 else:
  marks = int(input("Enter marks:"))

  student = {
    "name": name,
    "marks": marks
  }
 students.append(student)
 
for student in students:
  
  print(students)
def view_student():
    pass
def search_student():
    pass
def calculate_student():
    total_marks = sum(marks)
    percentage = (marks/total_marks)*100 
def exit():
    pass'''