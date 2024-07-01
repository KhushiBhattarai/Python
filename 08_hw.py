# Write a Python program that prompts the user to enter a number corresponding to a month 
# (1 for January, 2 for February, ..., 12 for December). 
# The program should then display the name of the month based on the number entered.

month = int(input("Enter the number for month between[1-12]: "))

if (month == 1):
    print(f"The {month}st month is: January")
elif (month == 2):
    print(f"The {month}nd month is: February")
elif (month == 3):
    print(f"The {month}rd month is: March")
elif (month == 4):
    print(f"The {month}th month is: April")
elif (month == 5):
    print(f"The {month}th month is: May")
elif (month == 6):
    print(f"The {month}th month is: June")
elif (month == 7):
    print(f"The {month}th month is: July")
elif (month == 8):
    print(f"The {month}th month is: August")
elif (month == 9):
    print(f"The {month}th month is: September")
elif (month == 10):
    print(f"The {month}th month is: October")
elif (month == 11):
    print(f"The {month}th month is: November")
elif (month == 12):
    print(f"The {month}th month is: December")
else:
    print("Select number between[1-12]")
    