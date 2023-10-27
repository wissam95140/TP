from password_strength import PasswordStrengthTester
from password_generator import PasswordGenerator

def main():
    # Demander à l'utilisateur de spécifier les critères du mot de passe
    password_length = int(input("Longueur du mot de passe : "))
    num_lower = int(input("Nombre de lettres minuscules : "))
    num_upper = int(input("Nombre de lettres majuscules : "))
    num_digits = int(input("Nombre de chiffres : "))
    num_special = int(input("Nombre de caractères spéciaux : "))

    # Générer un mot de passe
    generator = PasswordGenerator()
    generated_password = generator.generate_password(password_length, num_lower, num_upper, num_digits, num_special)
    
    # Tester la force du mot de passe
    tester = PasswordStrengthTester(generated_password)
    entropy = tester.calculate_entropy()
    strength = tester.test_password_strength()

    print("Mot de passe généré :", generated_password)
    print("Entropie :", entropy)
    print("Force :", strength)

if __name__ == "__main__":
    main()
