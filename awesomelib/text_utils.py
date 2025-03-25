def is_palindrome(text):
    """Sprawdza, czy tekst jest palindromem."""
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

def count_words(text):
    """Zlicza słowa w podanym tekście."""
    return len(text.split())