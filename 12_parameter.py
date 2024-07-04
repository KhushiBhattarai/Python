# WAP to print odd number between 100 - 150 using start and end

def odd(start,end):
    for i in range(start, end+1):
        if (i % 2 != 0):
            print(i)

starting = 100
ending = 150

odd(starting,ending)
print("----------")
odd(0,50)