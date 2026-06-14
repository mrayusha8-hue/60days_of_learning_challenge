#PYTHON OBJECT ORIENTED PROGRAMMING
#Classes

class Student: 
 def __init__(self,name,course,fee):
    self.name = name
    self.course = course
    self.fee = fee
    self.email = name + '@gmail.com'
    
std_1 = Student('Tom','C1',2000)
std_2 = Student('Jack','C2', 3000)

print(std_1.email)
print(std_2.email)
