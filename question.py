class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()

# Liste de questions et réponses
questions_data = [
    Question("En quelle année a eu lieu la première Coupe du Monde de football ?", ["a) 1928", "b) 1930", "c) 1934"], "a"),
    Question("Quel joueur de football a remporté le plus de Ballons d'Or FIFA ?", ["a) Lionel Messi", "b) Cristiano Ronaldo", "c) Pelé"], "a"),
    Question("Quelle équipe de football a remporté le plus de Coupe du Monde ?", ["a) Brésil", "b) Allemagne", "c) Argentine"], "a"),
    Question("Quelle nation a remporté le plus de titres de l'Euro (Championnat d'Europe de football) ?", ["a) Allemagne", "b) France", "c) Espagne"], "b"),
    Question("Qui détient le record du nombre de buts marqués en une seule saison de la Liga espagnole de football ?", ["a) Lionel Messi", "b) Cristiano Ronaldo", "c) Luis Suárez"], "a"),
    Question("Quel est le club de football avec le plus grand nombre de victoires en Ligue des champions de l'UEFA ?", ["a) Real Madrid", "b) FC Barcelone", "c) Manchester United"], "a"),
    Question("Quel pays a remporté la Coupe d'Afrique des Nations (CAN) de football le plus de fois ?", ["a) Egypte", "b) Cameroun", "c) Nigeria"], "b"),
    Question("Quel joueur a marqué le plus de buts lors d'une seule Coupe du Monde de la FIFA ?", ["a) Just Fontaine", "b) Pelé", "c) Gerd Müller"], "a"),
    Question("Quelle équipe de football a remporté le plus de titres de Premier League anglaise ?", ["a) Manchester United", "b) Liverpool", "c) Chelsea"], "a"),
    Question("Qui est le meilleur buteur de tous les temps en Ligue 1 française de football ?", ["a) Edinson Cavani", "b) Zlatan Ibrahimović", "c) Lionel Messi"], "c"),

]
