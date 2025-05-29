def validate_positive_float(value):
    """Valide qu'une valeur est un float positif"""
    try:
        num = float(value)
        return num > 0
    except ValueError:
        return False

def validate_positive_int(value):
    """Valide qu'une valeur est un entier positif"""
    try:
        num = int(value)
        return num > 0
    except ValueError:
        return False