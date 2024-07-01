import datetime
import datetime_nepali

year = int(input("Enter the Nepali year: "))
month = int(input("Enter the Nepali month: "))
day = int(input("Enter the Nepali day: "))
date = datetime_nepali.date(year,month,day).to_datetime_date()
print(f"English date is: {date}")

print(datetime_nepali.date(2085,6,22).calendar())