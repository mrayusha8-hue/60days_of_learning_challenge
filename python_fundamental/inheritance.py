#Inheritance
# Create the Animal class
class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    print(self.name)

# Create the Dog class (inherits from Animal)
class Dog(Animal):
  pass

# Create an object
d1 = Dog("Rex")

# Call the speak method
d1.speak()
