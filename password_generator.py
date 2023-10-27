import random
import string
import math

class PasswordGenerator:
    def generate_password(self, length, num_lower, num_upper, num_digits, num_special):
        total_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

        # Vérifiez si la somme des critères respecte la longueur du mot de passe
        if length < num_lower + num_upper + num_digits + num_special:
            print("Longueur du mot de passe invalide. Veuillez ajuster les critères.")
            return None
        
        # Générer des caractères en fonction des critères spécifiés
        lowercase = ''.join(random.choices(string.ascii_lowercase, k=num_lower))
        uppercase = ''.join(random.choices(string.ascii_uppercase, k=num_upper))
        digits = ''.join(random.choices(string.digits, k=num_digits))
        special_chars = ''.join(random.choices(string.punctuation, k=num_special))

        # Concaténer les caractères générés pour former le mot de passe
        all_characters = lowercase + uppercase + digits + special_chars
        remaining_length = length - len(all_characters)
        additional_chars = ''.join(random.choices(all_characters, k=remaining_length))
        generated_password = lowercase + uppercase + digits + special_chars + additional_chars

        # Mélanger le mot de passe pour plus de sécurité
        password_list = list(generated_password)
        random.shuffle(password_list)
        final_password = ''.join(password_list)
        return final_password
    #Calcul de la force du mot de passe basé sur l'entropie
    def calculate_password_strength(self, length, num_lower, num_upper, num_digits, num_special):
        total_characters = len(string.ascii_lowercase) + len(string.ascii_uppercase) + len(string.digits) + len(string.punctuation)
        total_combinations = total_characters ** length
        password_strength = total_combinations
        password_entropy = math.log2(total_combinations)
        return password_strength, password_entropy

    def generate_passphrase(self, wordlist, num_words):
        if num_words > len(wordlist):
            print("Nombre de mots demandés supérieur à la taille de la wordlist.")
            return None
        passphrase_words = random.sample(wordlist, num_words)
        passphrase = ' '.join(passphrase_words)
        return passphrase

# Utilisation de la classe PasswordGenerator
if __name__ == "__main__":
    # Exemple d'utilisation pour générer un mot de passe et une passphrase
    generator = PasswordGenerator()
    
    # Demander à l'utilisateur les critères pour le mot de passe
    password_length = int(input("Longueur du mot de passe : "))
    num_lower = int(input("Nombre de lettres minuscules : "))
    num_upper = int(input("Nombre de lettres majuscules : "))
    num_digits = int(input("Nombre de chiffres : "))
    num_special = int(input("Nombre de caractères spéciaux : "))

    # Générer un mot de passe
    generated_password = generator.generate_password(password_length, num_lower, num_upper, num_digits, num_special)
    print("Mot de passe généré :", generated_password)
    
    # Calculer la force et l'entropie du mot de passe
    password_strength, password_entropy = generator.calculate_password_strength(password_length, num_lower, num_upper, num_digits, num_special)
    print("Force du mot de passe :", password_strength)
    print("Entropie du mot de passe (en bits) :", password_entropy)

    # Générer une passphrase
    wordlist = ["chat", "chien", "maison", "arbre", "soleil", "pluie", "ordinateur", "voiture"]
    num_words_in_passphrase = 4
    generated_passphrase = generator.generate_passphrase(wordlist, num_words_in_passphrase)
    print("Passphrase générée :", generated_passphrase)

    