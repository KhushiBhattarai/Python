name = 'Khushi Bhattarai'

split = name.split(" ") #split can be done by many methods one is space, comma,etc...
print(split)
print(len(split))

#Find the first name and last name
full_name = input("Enter your full name: ")
split = full_name.split(" ") 
print(f"The full name is: {split}")

first_name = split[0]
last_name = split[1]

print(first_name)
print(last_name)
# if there is no middle name then it will give the error in this code. So we didnot put the middle name function here

names = 'khushi,viru,meow'
splited = names.split(",")
print(splited)