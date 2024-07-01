# create program to generate random number between -10 to -20

import random

random_num = random.randint(-20,-10)
user = int(input("Enter the random number between the -20 to -10: ")) 

if user == random_num:
    print("Congratulation you guessed the right number")

else:
    print("The number you guessed is wrong")
    
print(f"The actual random number is: {random_num}")