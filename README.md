# python-intro

Ten projekt to zestaw pięciu prostych funkcji w Pythonie wraz z testami jednostkowymi. Wszystko zostało stworzone zgodnie z podejściem **Test-Driven Development (TDD)** – czyli najpierw piszemy testy, a dopiero potem kod, który ma je „zadowolić”.

---

#Co zawiera projekt?

W folderze `app/` znajdziesz dwa pliki:

- `app.py` – tutaj są funkcje, które zrobiłem
- `test_app.py` – a tutaj testy, które sprawdzają czy te funkcje działają poprawnie

---

#Jakie funkcje napisałem?

1. **Sprawdzanie adresu e-mail**  
   Funkcja `is_valid_email()` sprawdza, czy adres e-mail wygląda jak należy.

2. **Obliczanie pola prostokąta**  
   `calculate_rectangle_area()` przyjmuje długość i szerokość, a zwraca pole. Jeśli podasz ujemne liczby, to rzuca błędem.

3. **Filtrowanie i sortowanie listy**  
   `filter_and_sort_list()` bierze listę liczb i próg, i zwraca tylko te liczby, które są większe niż próg – posortowane rosnąco.

4. **Konwersja daty**  
   `convert_date_format()` zamienia datę z jednego formatu na inny (np. z `22-03-2025` na `2025/03/22`).

5. **Sprawdzanie palindromu**  
   `is_palindrome()` sprawdza, czy tekst czytany od tyłu jest taki sam. Ignoruje spacje, wielkość liter i znaki specjalne.

---
