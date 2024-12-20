userInput = int(input("Gebe die Zahl an, die geprüft werden soll, ob es sich um eine Primzahl handelt: "))

if userInput > 1:
    is_prime = True
    for i in range(2, int(userInput**0.5) + 1):
        if userInput % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{userInput} ist eine Primzahl.")
    else:
        print(f"Bei der Zahl {userInput} handelt es sich um keine Primzahl.")
else:
    print(f"Bei der Zahl {userInput} handelt es sich um keine Primzahl.")

# 211 und 293 ist eine Primzahl. Zum Testen
# 198 und 291 ist keine Primzahl.