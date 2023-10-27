import random

class QCM:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_quiz(self):
        random.shuffle(self.questions)
        for i, question in enumerate(self.questions):
            print(f"Question {i + 1}: {question.question}")
            for option in question.options:
                print(option)
            user_answer = input("Votre réponse (a/b/c) : ")
            if question.is_correct(user_answer):
                print("Bonne réponse!\n")
                self.score += 1
            else:
                print(f"Mauvaise réponse. La réponse correcte était {question.correct_answer}.\n")

    def display_score(self):
        print(f"Votre score final est de {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    from questions import questions_data

    qcm = QCM(questions_data)
    qcm.start_quiz()
    qcm.display_score()
