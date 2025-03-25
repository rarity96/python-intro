import unittest
from app import (
    is_valid_email,
    calculate_area_rectangle,
    filter_even_numbers,
    convert_date_format,
    is_palindrome
)

class TestFunctions(unittest.TestCase):

    def setUp(self):
        # Dane używane w wielu testach
        self.emails = [
            ("test@example.com", True),
            ("noatsign.com", False),
            ("@nodomain", False)
        ]
        self.dates = [
            ("25-12-2020", "2020/12/25"),
            ("01-01-2000", "2000/01/01"),
        ]
        self.palindromes = [
            ("Kajak", True),
            ("A man, a plan, a canal: Panama", True),
            ("Hello", False),
        ]

    # Testy e-maili
    def test_email_validation(self):
        for email, expected in self.emails:
            with self.subTest(email=email):
                self.assertEqual(is_valid_email(email), expected)

    # Testy pola prostokąta
    def test_calculate_area(self):
        self.assertEqual(calculate_area_rectangle(5, 10), 50)
        self.assertEqual(calculate_area_rectangle(0, 10), 0)
        with self.assertRaises(ValueError):
            calculate_area_rectangle(-1, 5)

    # Testy filtrowania liczb parzystych
    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])
        self.assertEqual(filter_even_numbers([2, "4", 6]), [2, 6])

    # Testy konwersji dat
    def test_convert_date_format(self):
        for date_in, expected in self.dates:
            with self.subTest(date=date_in):
                self.assertEqual(convert_date_format(date_in), expected)
        with self.assertRaises(ValueError):
            convert_date_format("2020-12-25")

    # Testy palindromów
    def test_is_palindrome(self):
        for text, expected in self.palindromes:
            with self.subTest(text=text):
                self.assertEqual(is_palindrome(text), expected)


if __name__ == '__main__':
    unittest.main()
