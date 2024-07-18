# Global dictionary and counter
game_data = {}
counter = 1

def add():
    global counter
    question = input("Enter question: ")
    option1 = input("Enter opt 1: ")
    option2 = input("Enter opt 2: ")
    right_answer = input("Enter Right Answer: ")

    game_data[counter] = {
        'question': question,
        'option1': option1,
        'option2': option2,
        'right_answer': right_answer
    }
    counter += 1
    print("Question added successfully!")

def read():
    if not game_data:
        print("No questions available.")
    else:
        for i, j in game_data.items():
            print(f"{i}) {j['question']}")
            print(f"A: {j['option1']}")
            print(f"B: {j['option2']}")
            answer = input("Enter answer: ")
            if j['right_answer'] == answer:
                print("Correct Answer!!")
            else:
                print(f"Wrong Answer. The correct answer is: {j['right_answer']}")

def delete():
    if not game_data:
        print("No question for delete!!")
    else:
        for i, j in game_data.items():
            print(f"{i} , {j['question']}")
        delete = int(input("Enter question number to delete: "))
        if delete in game_data:
            del game_data[delete]
            print(f"Deleted question {delete} successfully!!")
        else:
            print("Invalid question number!!")
