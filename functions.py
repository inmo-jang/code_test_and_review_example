def add(a, b):
    """Add two numbers."""
    return a + b

def minus(a, b):
    """Subtract b from a."""
    return a - b

def power(a, b):
    """Power a by b"""
    return a ** b

def multiply(a, b):
    """Multiply a and b"""
    return a * b

def avg(a, b):
    """Average of a and b"""
    return (a + b) / 2

def gcd(a, b):
    while b:  # b가 0이 될 때까지 a와 b를 나누며 반복
        a, b = b, a % b
    return a

