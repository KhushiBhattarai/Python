no_of_days = int(input("Enter the number of day from[1-7]: "))

if(no_of_days == 1):
    print(f"{no_of_days}st day is Sunday")
elif(no_of_days == 2):
    print(f"{no_of_days}nd day is Monday")
elif(no_of_days == 3):
    print(f"{no_of_days}rd day is Tuesday")
elif(no_of_days == 4):
    print(f"{no_of_days}th day is Wednesday")
elif(no_of_days == 5):
    print(f"{no_of_days}th day isThursday")
elif(no_of_days == 6):
    print(f"{no_of_days}th day is Friday")
elif(no_of_days == 7):
    print(f"{no_of_days}th day is Saturday")
else:
    print("Choose the number between[1-7]")