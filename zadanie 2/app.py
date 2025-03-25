import re
from datetime import datetime

def is_valid_email(email):
    """Sprawdza, czy e-mail jest poprawny."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def calculate_area_rectangle(length, width):
    """Oblicza pole prostokąta."""
    if length < 0 or width < 0:
        raise ValueError("Wymiary nie mogą być ujemne.")
    return length * width

def filter_even_numbers(numbers):
    """Zwraca listę parzystych liczb z podanej listy."""
    return [n for n in numbers if isinstance(n, int) and n % 2 == 0]

def convert_date_format(date_str):
    """Konwertuje datę z formatu DD-MM-YYYY na YYYY/MM/DD."""
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        return date_obj.strftime("%Y/%m/%d")
    except ValueError:
        raise ValueError("Nieprawidłowy format daty. Użyj DD-MM-YYYY.")

def is_palindrome(text):
    """Sprawdza, czy podany tekst jest palindromem."""
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]