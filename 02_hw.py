# Write down what you spend each day from Sunday to Saturday, add them up to find the total for the week, 
# and figure out the average amount spent per day

Sunday = 1000
Monday = 1500
Tuesday = 800
Wednesday = 340
Thursday = 500
Friday = 900
Saturday = 2500

Total_expenses = Sunday + Monday + Tuesday + Wednesday + Thursday + Friday + Saturday
print(f"The total expenses of a week is: {Total_expenses}")

Average_expenses = (Total_expenses/7)
print(f"The average expenses per day is: {Average_expenses}")

## Second Method
expenses = [1000,1500,800,340,500,900,2500]
total_expenses = expenses[0] + expenses[1] + expenses[2] + expenses[3] + expenses[4] + expenses[5] + expenses[6]
average_expenses = (total_expenses/7)
print("Second Method")
print(f"The total expenses is: {total_expenses}")
print(f"The average expenses per day is: {average_expenses}")