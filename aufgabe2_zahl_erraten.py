import random

def number_guessing_game():
    correct_number = random.randint(1, 10)
    
    print("Willkommen beim Zahlenratespiel!")
    print("Ich habe mir eine Zahl zwischen 1 und 10 überlegt. Kannst du diese erraten?")

    while True:
        try:
            user_input = int(input("Gebe deine geschätzte Zahl ein: "))

            if user_input < 1 or user_input > 10:
                print("Bitte gebe eine Zahl zwischen 1 und 10 ein.")
                continue

            if user_input == correct_number:
                print("Glückwunsch! Du hast die richtige Zahle erraten.")
                break
            else:
                print("Falsch geraten! Versuche es erneut.")
        except ValueError:
            print("Dies ist keine gültige Zahl. Bitte gebe eine Zahl zwischen 1 und 10 ein.")

if __name__ == "__main__":
    number_guessing_game()