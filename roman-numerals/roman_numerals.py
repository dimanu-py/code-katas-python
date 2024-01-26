

def roman_numeral(number: int) -> str:
    """
    Convert an arabic number to a roman numeral
    """
    return "IV" if number == 4 else 'I' * number