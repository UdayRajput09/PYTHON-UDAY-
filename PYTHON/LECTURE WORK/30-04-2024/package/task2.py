from task1 import *

while True:
    menu="""


    ----press menu----

    1.reverse
    2.length
    3.middle
    4.concat
    5.exit


"""

    print(menu)
    c = int(input("Enter Choice : "))

    if c == 1:
        srev()
    elif c == 2:
        slen()
    elif c == 3:
        middle()
    elif c == 4:
        concat()
    elif c == 5:
        print("Thankyou for using!!")
        break;
    else:
        print("Invalid choice!!")
        break
