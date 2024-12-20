def check_even_or_odd():
    print("Willkommen beim GERADE oder UNGERADE Prüfer!")
    
    while True:
        try:
            user_input = int(input("Gebe eine Nummer ein: "))

            if user_input % 2 == 0:
                print(f"Die Zahl {user_input} ist gerade.")
            else:
                print(f"Die Zahl {user_input} ist ungerade.")

            another = input("Möchtest du eine andere Nummer prüfen? (ja/nein): ").strip().lower()
            if another != 'ja':
                print("Auf Wiedersehen!")
                break
        except ValueError:
            print("Ungültige Eingabe. Bitte gebe eine gültige Nummer ein.")

if __name__ == "__main__":
    check_even_or_odd()