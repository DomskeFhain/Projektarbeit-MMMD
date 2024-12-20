def celsius2fahrenheit():

    print("Konvertiert Celsius in Fahrenheit um.")
    c_input = float(input("Gib die die '°C' als Zahl an, die umgerechnet werden soll: "))
    fahrenheit_temp = celsius2fahrenheit(c_input)
    print(f"{c_input}°C sind {fahrenheit_temp}°F")
    return (c_input * 9/5) + 32

def fahrenheit2celsius():

    print("Konvertiert Fahrenheit in Celsius.")
    f_input = float(input("Gib die °F als Zahl ein, die umgerechnet werden soll: "))
    celsius_temp = celsius2fahrenheit(f_input)
    print(f"{f_input}°F sind {celsius_temp}°C")
    return (f_input - 32) * 5/9

def auswahlmenü():

    user = input("Was möchtest du umgerechnet habe? // 1 Celsius zu Fahrenheit / 2 Fahrenheit zu Celsius // : ")

    if user == "1":
        celsius2fahrenheit()
    elif user == "2"
        fahrenheit2celsius()
    else:
        print("Ungültige Eingabe")

auswahlmenü()

