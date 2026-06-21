#Polymorphism
# Create the Student class
class Student:
  def name(self):
    print("Tom")

# Create the Employee class
class Employee:
  def name(self):
    print("Jack")

# Create objects and loop
s1 = Student()
e1 = Employee()

for person in (s1, e1):
  person.name()
