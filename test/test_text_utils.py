import unittest
from awesomelib.text_utils import is_palindrome, count_words

class TestTextUtils(unittest.TestCase):
    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("Kajak"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("Python"))

    def test_count_words(self):
        self.assertEqual(count_words("Ala ma kota"), 3)