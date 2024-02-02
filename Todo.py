def menu():
    print()
    print("Welcome")
    print("Enter 1 to add an item")
    print("Enter 2 to remove an item")
    print("Enter 3 to view the item")
    print("Enter 4 to exit the program")
    print()
   
myList = []
userInput = ''
while userInput !='4':
    menu();
    userInput= input("Please enter the valid choice: ")
    if userInput== '1':
       addItem = input("What would like to add: ")
       myList.append(addItem)
       print("You have added ", addItem)
    elif(userInput=='2'):
        removeItem = input("What would you like to remove: ")
        if removeItem in myList:
            myList.remove(removeItem)
            print("You have removed ", removeItem)
        else:
            print("Cannot find ", removeItem, ' in your list')
       
    elif(userInput == '3'):
        if(len(myList)>0):
            for x in myList:
                print("Your To-Do List: ", x)
        else:
            print('Add item to view the list')
    elif(userInput== '4'):
        print("Thankyou")
    else:
        print("Please choose the valid option")
      
