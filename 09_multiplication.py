# print multiplication by asking user

start = int(input("Enter the starting number: "))
end = int(input("ENter the ending number: "))

for i in range(start,end+1):
    for j in range(0,10):
        print(f" {i} * {j+1} = {i*(j+1)}")
    print("\n ---- \n")