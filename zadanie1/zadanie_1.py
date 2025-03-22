"""Funkcja wbudowana zip()
Łączy elementy z wielu iterowalnych obiektów (np. list) w krotki.
📚 Dokumentacja: https://docs.python.org/3/library/functions.html#zip


    Moduł random
Służy do generowania liczb losowych, losowego wyboru elementów itd.
📚 Dokumentacja: https://docs.python.org/3/library/random.html


Wyjątek ZeroDivisionError
Występuje, gdy dzielimy przez zero.
📚 Dokumentacja: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
"""


# zadanie1.py

# Łączenie dwóch list za pomocą zip()
# Dokumentacja: https://docs.python.org/3/library/functions.html#zip
names = ["Anna", "Jan", "Ola"]
ages = [25, 30, 22]
people = list(zip(names, ages))
print("Lista osób:", people)

# Użycie funkcji z modułu random
# Dokumentacja: https://docs.python.org/3/library/random.html
import random
random_person = random.choice(people)
print("Wylosowana osoba:", random_person)

# Obsługa wyjątku ZeroDivisionError
# Dokumentacja: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
try:
    number = int(input("Podaj liczbę: "))
    result = 100 / number
    print("Wynik dzielenia:", result)
except ZeroDivisionError:
    print("Błąd: Nie można dzielić przez zero!")