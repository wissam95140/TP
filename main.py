from qcm import QCM

from question import questions_data

if __name__ == "__main__":
    qcm = QCM(questions_data)
    qcm.start_quiz()
    qcm.display_score()
