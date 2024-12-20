
# Aufgabe4:Wörter zählen (aufgabe4_woerter_zaehlen.py)
# Schreibt ein Programm,das die Anzahl der Wörter in einem eingegebenen Satz zählt'

# Aufgabe 4: Wörter zählen

# Benutzereingabe: Einen Satz eingeben
satz = input("Bitte gib einen Satz ein: ")

# Die Eingabe wird in eine Liste von Wörtern aufgeteilt
woerter = satz.split()

# Die Anzahl der Wörter wird ermittelt
anzahl_woerter = len(woerter)

# Ausgabe der Anzahl der Wörter
print(f"Der Satz enthält {anzahl_woerter} Wörter.")
