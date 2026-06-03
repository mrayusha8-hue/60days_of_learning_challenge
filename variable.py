#variables using f-strings

#string variable
name="Timsha"
print(f"My name is{name}")

#integer variable
age=20
print(f"She is {age}.")

#float variable
money=100.50
print(f"She has ${money:.2f}.")

#boolean variable
is_employee=True
print(f"Is she an employee? {is_employee}")


# type() -> used to check the data type of a variable
print(type(name))
print(type(is_employee))


#Typecasting-> converting one data type to another
'''name=int(name) #this gives error as name is a string and cannot be converted to an integer'''
#int to str
age=age+1
age=str(age)
print(age)

#str to int
age=int(age)
print(age)
print(type(age))

#int to float
money=float(money)
print(type(money))
print(f"She has around ${money:.2f}.") #format as a floating-point number with 2 digits after the decimal

#string to bool
is_employee=str(is_employee)
print(type(is_employee))


#input() -> used to take user input

address=input("Enter your address : ")
print(f"She lives at{address}.")

salary=float(input("Enter your salary: "))
salary=float(salary+5000)
print(f"Congratulations! Your new salary is ${salary:.2f}.")

age=int(input("Enter your age: "))
print(f"You are {age} years old.")
