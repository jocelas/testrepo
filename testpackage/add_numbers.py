import numpy as np

def add(a, b):
    """Adds two numbers and returns the result rounded to the nearest integer.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        int: The sum of a and b, rounded to the nearest integer.
    """
    return np.round(a + b)
