todos = []
total_todos = int(input("Enter total number of todo list: "))

for i in range(1,(total_todos+1)):
    todo =(input(f"Enter the {i} todo: "))
    todos.append(todo)

print("\n ------ \n")
print("All todos are;")

for todo in todos:
    print(todo)