def menu():
    arrMenu = ("  Menu", "1 - Calculator", "2 - Registration", "3 - Game of Tic")
    try:
        for i in arrMenu:
            print(i)
            intMenu = int(input("Enter the value for access: "))
  
            if(intMenu==1):
                print("Calculator")
            elif(intMenu==2):
                print("Registration")
            elif(intMenu==3):
                print("Game")
            else:
                print ("Choose the item as numbered.")
    except:
        print("Invalid value.")

menu()

