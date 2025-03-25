def filter_even(numbers):
    """Zwraca tylko liczby parzyste z listy."""
    return [n for n in numbers if isinstance(n, int) and n % 2 == 0]

def flatten_list(nested_list):
    """Spłaszcza listę zagnieżdżoną (jednopoziomowo)."""
    return [item for sublist in nested_list for item in sublist]