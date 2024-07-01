#Add your Electricity Bill From Jan dec In Dec in Dictionary and find total and average .
bill={
    'jan' : 150,
    'feb' : 90,
    'mar' : 87,
    'apr': 200,
    'may' : 136,
    'june': 345,
    'july' : 230,
    'aug' : 180,
    'sep' : 156,
    'oct' : 200,
    'nov': 90,
    'dec' : 102
}

total = sum(bill.values())

print(f"The total electricity bill from jan to dec is: {total}")
print(f"The average electricity bill from per month is: {total/12}")

print(f"The bill of nov is: {bill['nov']}")
