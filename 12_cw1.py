# WAP that print 70 to 100 but not [77,78,81]

# first method
# for i in range(70,101):
#     if (i==77):
#         continue
#     if (i==78):
#         continue
#     if (i == 81):
#         continue
#     print(i)

# second method
for i in range(70,101):
    if (i == 77) or (i == 78) or (i == 81):
        continue
    print(i)