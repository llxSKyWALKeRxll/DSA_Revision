queue = []
i = 0
while(i != 7):
    print("*** queue OPERATIONS ***")
    print("1. Create a new queue")
    print("2. Insert an element into the queue (top)")
    print("3. Insert an element into the queue (front)")
    print("4. Delete an element from the queue (top)")
    print("5. Delete an element from the queue (front)")
    print("6. Display queue")
    print("7. Exit")
    i = int(input("Your choice: "))
    if(i==1):
        #Create new queue
        queue = []
        print("A new queue has been created!\nqueue =", queue)

    elif(i==2):
        #Insert an element at top
        element = int(input("Enter the element that you want to insert at the top: "))
        queue.append(element)
        print("queue =", queue)
        pass
    
    elif(i==3):
        #Insert an element at front
        element = int(input("Enter the element that you want to insert at the front: "))
        queue.insert(0, element)
        print("queue =", queue)
        pass

    elif(i==4):
        #Delete an element at top
        del queue[-1]
        print("queue =", queue)
        pass

    elif(i==5):
        #Delete an element at front
        del queue[0]
        print("queue =", queue)
        pass

    elif(i==6):
        print("queue =", queue)

    elif(i>7):
        print("Invalid choice!")

    print()
print("See you later! =)")