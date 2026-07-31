
def addition(a, b):
    """Retourne la somme de a et b"""
    return a + b

def division(a, b):
    """Retourne le quotient de a divisé par b"""
    if b == 0:
        raise ValueError("La division par zéro n'est pas permise.")
    return a / b
