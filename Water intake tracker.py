#Water intake tracker using if/else statements
print("Welcome to the Water Intake Tracker!")

#Taking user input 
weight=float(input(" Enter your weight in kg: "))
activity_level=input("Were you active today? (Yes/No): ").lower()

#Calculating water intake: 
water_intake=weight*30  #general recommendation is 30ml of water per kg of body weight
if activity_level=="yes":
    water_intake+=500  #add 500ml for active days
else:
    water_intake+=0  #no additional water needed for inactive days
    
 #Converting water intake to liters
water_intake_liters=water_intake/1000

#Output
print(f"You should drink approximately {water_intake_liters:.2f} liters of water today.")

#Input for actual water intake
actual_water_intake=float(input("Enter the amount of water you drank today in liters: "))

#Feedback based on water intake
if actual_water_intake<water_intake_liters:
    print("You should drink more water to stay hydrated!✊")
elif actual_water_intake==water_intake_liters:
    print("Good job! You're meeting your water intake needs.👍")      
else:
    print("Great! You're drinking plenty of water!👏")
