#in list[] we can change variables,support duplicate and order form
todo_list = ['python','dyango','web']
todo_list.append ("flutter") #it add on the value in the list

todo_list[0] = 'mobileapp'

todo_list.pop()  #pop removes the last item from the list

for i in todo_list:
    print(i)