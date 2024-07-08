
# creating class name Game
class Game:
    def __init__(self):
        self.dic = {}
        self.counter = 1

    # creating add function
    def add(self):
        question = input("Enter question: ")
        option1 = input("Enter opt 1: ")
        option2 = input("Enter opt 2: ")
        right_answer = input("Enter Right Answer: ")

        self.dic[self.counter] = {
            'question': question,
            'option1': option1,
            'option2': option2,
            'right_answer': right_answer
        }
        self.counter += 1
        print("Question added successfully!")

    # creating read function
    def read(self):
        if not self.dic:
            print("No questions available.")
        else:
            for i, j in self.dic.items():
                print(f"{i}) {j['question']}")
                print(f"A: {j['option1']}")
                print(f"B: {j['option2']}")
                answer = input("Enter answer: ")
                if j['right_answer'] == answer:
                    print("Correct Answer!!")
                else:
                    print(f"Wrong Answer. The correct answer is: {j['right_answer']}")


    # creating delete function
    def delete(self):
        if not self.dic:
            print("No question for delete!!")
        else:
            for i, j in self.dic.items():
                print(f"{i} , {j['question']}")
            delete = int(input("Enter question number to delete: "))
            if delete in self.dic:
                del self.dic[delete]
                print(f"Deleted question {delete} successfully!!")
            else:
                print("Invalid question number!!")
