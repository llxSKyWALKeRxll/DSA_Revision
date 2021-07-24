stack = []
i = 0
while(i != 7):
    print("*** STACK OPERATIONS ***")
    print("1. Create a new stack")
    print("2. Insert an element into the stack (top)")
    print("3. Insert an element into the stack (front)")
    print("4. Delete an element from the stack (top)")
    print("5. Delete an element from the stack (front)")
    print("6. Display stack")
    print("7. Exit")
    i = int(input("Your choice: "))
    if(i==1):
        #Create new stack
        stack = []
        print("A new stack has been created!\nstack =", stack)

    elif(i==2):
        #Insert an element at top
        element = int(input("Enter the element that you want to insert at the top: "))
        stack.append(element)
        print("stack =", stack)
        pass
    
    elif(i==3):
        #Insert an element at front
        element = int(input("Enter the element that you want to insert at the front: "))
        stack.insert(0, element)
        print("stack =", stack)
        pass

    elif(i==4):
        #Delete an element at top
        del stack[-1]
        print("stack =", stack)
        pass

    elif(i==5):
        #Delete an element at front
        del stack[0]
        print("stack =", stack)
        pass

    elif(i==6):
        print("stack =", stack)

    elif(i>7):
        print("Invalid choice!")

    print()
print("See you later! =)")
