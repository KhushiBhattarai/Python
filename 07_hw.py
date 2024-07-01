#Create Software that convert English Date to Nepali Date
import nepali_datetime
from datetime import date


year = int(input("Enter the English year: "))
month = int(input("Enter the English month: "))
day = int(input("Enter the English day: "))


conversion_date = date(year, month, day)

nepali_date = nepali_datetime.date.from_datetime_date(conversion_date)


print(f"Nepali date is: {nepali_date}")
