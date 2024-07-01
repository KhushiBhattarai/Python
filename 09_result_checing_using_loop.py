symbol_nos = {
    '019222K' : '4',
    '020222L' : '3',
    '018222M' : '2'
}

symbol_no = input("Enter your symbol number: ")

result = ""

for i in symbol_nos.keys():
    if i == symbol_no:
        result = symbol_nos[i]
        break
    else:
        result = ""

if result != "":
    print(f"The result of symbol number '{symbol_no}' is: {result}")
else:
    print(f"The result of symbol number '{symbol_no}' is not found")