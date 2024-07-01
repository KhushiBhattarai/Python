# Ask user to enter n number of fruits and display all of them

fruits = []

total_fruits = int(input("Enter the total number of fruits: "))

for i in range(1,(total_fruits+1)):
    fruit = input(f"The {i} is: ")
    fruits.append(fruit)

print("\n----\n")
print("All the fruits are: ")

for fruit in fruits:
    print(fruit)