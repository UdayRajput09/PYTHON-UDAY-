def fun():

    while True:
        menu = """
        -------Menu-------
        Press 1 for Addition
        Press 2 for Subtraction
        Press 3 for Multiplication
        Press 4 for Exit
    """

        print(menu)
        choice = int(input("Enter Choice : "))

        if choice == 1:
            num1 = int(input("Enter Number 1 : "))
            num2 = int(input("Enter Number 2 : "))

            print("Addition : ",num1 + num2)
            break


        elif choice == 2:
            num1 = int(input("Enter Number 1 : "))
            num2 = int(input("Enter Number 2 : "))

            print("Subtraction : ",num1 - num2)
            break

        elif choice == 3:
            num1 = int(input("Enter Number 1 : "))
            num2 = int(input("Enter Number 2 : "))

            print("Multiplication : ",num1 * num2)
            break
        
        elif choice == 4:
            print("Thankyou for using!!")
            break
        
        else:
            print("Invalid choice!!\nPlease enter choice again")
        


fun()   
c = input("Calculate again , Enter y/n : ")

if c == "y" or c == "Y":
    fun()
