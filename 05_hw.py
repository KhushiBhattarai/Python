# Create a Python program that converts Nepali currency to USD, Euro, and Japanese Yen;
# for example, if you enter the amount in NRS as 5000, it should display the converted amounts as USD $45, Euro €43, and Japanese ¥8454.


user = float(input("Enter amount in Nrs: "))
one_usd_in_Nrs = 0.0075

USD = user * one_usd_in_Nrs
print(f"The usd amount of Nepali Rs {user} is: ${USD}")

one_euro_in_Nrs = 0.0070
Euro = user * one_euro_in_Nrs
print(f"The euro amount of Nepali Rs {user} is:  €{Euro} ")

one_japanese_in_Nrs = 1.20
Japanese = user * one_japanese_in_Nrs
print(f"The japanese amount of Nepali Rs {user} is:  ¥{Japanese} ")

