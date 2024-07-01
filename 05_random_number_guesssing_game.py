import random

random_number = random.randint(1,20)
user = int(input("Enter the random number between 1 to 20: "))
print(f"The actualnumber is : {random_number}")


#Q. why doo we use int()?
#Ans:  input("Enter the random number between 1 to 20: ") prompts the user to enter a number. The input is returned as a "string".
# int(...) converts this string to an integer so it can be compared with random_number.