import math

class PasswordStrengthTester:
    def __init__(self, password):
        self.password = password if password is not None else ""
    
    def calculate_entropy(self):
        if self.password:
            # Calcul de l'entropie du mot de passe (basé sur les règles de l'ANSSI)
            entropy = len(self.password) * math.log2(len(set(self.password)))
            return entropy
        else:
            return 0  # Ou toute autre valeur par défaut que vous voulez assigner pour l'entropie d'un mot de passe vide
    
    def test_password_strength(self):
        # Évaluer la force du mot de passe (ex. faible, moyenne, forte)
        # Code à implémenter ici
        return "Forte"
