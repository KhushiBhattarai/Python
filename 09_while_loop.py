atm_pin = '1234'
user_pin = ''
attempt = 0

while atm_pin != user_pin:
    if attempt>0:
        print(f"Invalid pin! Total attempt is: {attempt}")
    user_pin = input("Enter the ATM pin: ")
    attempt = attempt + 1

print("Access granted")
print("How much do you want to withdraw?")