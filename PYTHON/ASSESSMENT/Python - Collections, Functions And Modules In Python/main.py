from logic import Game

obj = Game()

print("WELCOME TO TOPS QUIZ GAME CHALLENGE")

print("WELCOME MASTER")
print("SHAKE YOUR BRAIN AND ADD SOME CHALLENGING QUESTIONS")
menu = """
        MENU 
    press 1 for add question 
    press 2 for view questions
    press 3 for delete question
    press 4 for go to quiz cracker
    press 5 for exit
    """

while True:
        print(menu)
        c = int(input("Which operation would you like to perform: "))
        
        if c == 1:
            obj.add()
           
        elif c == 2:
            obj.read()
           
        elif c == 3:
            obj.delete()

        elif c == 4:
            print("Welcome quiz cracker\n")
            obj.read()


        elif c == 5:
            print("Thank you for using our app!!")
            break

        else:
            print("Invalid option, please try again.")

else:
    print("Please select from 1 or 2 ")
