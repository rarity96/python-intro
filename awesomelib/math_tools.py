def add(a, b):
    """Zwraca sumę dwóch liczb."""
    return a + b

def divide(a, b):
    """Dzieli liczbę a przez b. Zgłasza wyjątek przy dzieleniu przez zero."""
    if b == 0:
        raise ValueError("Nie można dzielić przez zero.")
    return a / b