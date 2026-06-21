#exception : the event that interrupts the execution of program(ZeoDivisionError,ValueError,TypeError)
#try,except,finally


try:
    number = int(input("Enter the number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Enter numbers only!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup:")
