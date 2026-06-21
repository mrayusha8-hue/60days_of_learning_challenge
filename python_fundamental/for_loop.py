#for loop execute block of code for a fixed number of times
#syntax
'''for x in range(5):
    print(x)'''
    
#Countdown timer program
import time
time_counter=int(input("Enter the time in seconds: "))
for i in range(time_counter,0,-1):# for reverse counting
    seconds = i % 60
    minutes = int(i/60)%60
    hours = int(i/3600)
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)
print("Time's up!")


