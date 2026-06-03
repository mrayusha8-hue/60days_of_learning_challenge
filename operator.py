#Arithmetic operators
p=3
q=2
print(p+q)
print(f"The difference between{q} and {p} is {q-p}")
print(f"The exponentiation: {p**q} ,the floor division: {p//q} ,the modulus: {p%q} ,the product: {p*q} ,the quotient: {p/q}")

#Augmented assignment operators
x=6
#print(f"x=x+1:{x+=1}, x=x-1:{x-=1}, x=x*2:{x*=2}, x=x/2:{x/=2}, x=x%2:{x%=2}, x=x//2:{x//=2}, x=x**2:{x**=2}") 
# -> Error:f-string doesn't support assignment expressions
x += 1
print(f"x=x+1:{x}")
x -= 1
print(f"x=x-1:{x}")
x *= 2
print(f"x=x*2:{x}")
x /= 2
print(f"x=x/2:{x}")
x %= 2
print(f"x=x%2:{x}")
x //= 2
print(f"x=x//2:{x}")
x **= 2
print(f"x=x**2:{x}")

#logical Operators
x=True
y=25
if x and y>20:
    print("Both conditions are true")
if x or y<20:
    print("At least one condition is true")
if not x:
    print("x is false")

#Comparison Operators
x=10
y=60
if x==y:
    print("x is equal to y")
elif x!=y:
    print("x is not equal to y")  
elif x>y:
    print("x is greater than y")    
elif x<y:
    print("x is less than y")   
elif x>=y:
    print("x is greater than or equal to y")
elif x<=y:
    print("x is less than or equal to y")
          


