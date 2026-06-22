#Define a function called greet that takes a name parameter and prints Hello, [name]!. Then call it with your own name.
def greet(name):
    print(" hello "+ name)
 
greet("rayusha")

#Write a function square(n) that returns the square of n. Then store the result in a variable and print it.
def square(n):
  return n**2

result=square(4)
print(result)

#Write a function power(base, exp=2) that returns base raised to exp. Show that calling power(5) and power(5, 3) give different results 
def power(base,exp=2):
    return base**exp

print(power(5))
print(power(5,3))

#Write a function is_even(n) that returns True if n is even and False otherwise. Use it inside an if statement
def is_even(n):
     return n%2==0
if is_even(7):
      print(True)
else:
       print(False)

#Write a function make_tag(text, tag='p') that returns an HTML string like <p>Hello</p>. Call it once without the tag argument and once with tag='h1'.
def make_tag(text, tag='p'):
    return f"<{tag}>{text}</{tag}>"

print(make_tag("hello"))

print(make_tag("Title",tag='h1'))

#Write a function clamp(value, low=0, high=100) that returns value kept within the range [low, high]. For example, clamp(150) should return 100.
def clamp(value, low=0, high=100):
  if value<low:
   return low
  elif value>high:
     return high
  else:
   return value

print(clamp(150))
print(clamp(-8))
print(clamp(50))
print(clamp(150,0,150))