#while loop execute block of code as long as condition is true
'''syntax
while condition:
print("block of code")'''

#compound interest calculator using while loop
principal=0, 
rate=0,
time=0
while True:
    principal=int(input("Enter the principal amount: "))
    if principal<0:
        print("Principal amount cannot be negative,enter a valid amount")
    else:
        break
while True:
    rate=float(input("Enter the rate of interest: "))
    if rate<0:
        print("Rate of interest cannot be negative,enter a valid rate")
    else:
        break
while True: 
    time=int(input("Enter the time in years: "))
    if time<0:
        print("Time cannot be negative,enter a valid time")
    else:
        break
    
Total_amount=float(principal*pow((1+rate/100),time))
print(f"Total amount after {time}years is: {Total_amount:.2f}")
Compund_interest=Total_amount-principal
print(f"Compound interest is: {Compund_interest:.2f}")