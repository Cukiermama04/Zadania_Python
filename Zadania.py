def kalkulator():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    operacja = input("Wybierz operację (+, -, *, /): ")

    match operacja:
        case "+":
            print(f"Wynik: {a + b}")
        case "-":
            print(f"Wynik: {a - b}")
        case "*":
            print(f"Wynik: {a * b}")
        case "/":
            if b != 0:
                print(f"Wynik: {a / b}")
            else:
                print("Błąd: Dzielenie przez zero!")
        case _:
            print("Nieznana operacja!")


def konwerter_temperatur():
    wybor = input("Wybierz konwersję (C – Celsjusz → Fahrenheit, F – Fahrenheit → Celsjusz): ").upper()
    temp = float(input("Podaj temperaturę: "))

    match wybor:
        case "C":
            wynik = temp * 1.8 + 32
            print(f"{temp}°C = {wynik}°F")
        case "F":
            wynik = (temp - 32) / 1.8
            print(f"{temp}°F = {wynik}°C")
        case _:
            print("Niepoprawny wybór!")


def srednia_ocen():
    n = int(input("Podaj liczbę ocen: "))
    suma = 0

    for i in range(n):
        ocena = float(input(f"Podaj ocenę {i + 1}: "))
        suma += ocena

    srednia = suma / n
    print(f"Średnia: {srednia:.2f}")

    if srednia >= 3.0:
        print("Uczeń zdał.")
    else:
        print("Uczeń nie zdał.")


def menu():
    print("\n=== MENU ===")
    print("1 - Prosty kalkulator")
    print("2 - Konwerter temperatur")
    print("3 - Średnia ocen ucznia")
    print("0 - Wyjście")

    wybor = input("Wybierz opcję: ")

    match wybor:
        case "1":
            kalkulator()
        case "2":
            konwerter_temperatur()
        case "3":
            srednia_ocen()
        case "0":
            print("Koniec programu.")
        case _:
            print("Niepoprawny wybór!")


while True:
    menu()
