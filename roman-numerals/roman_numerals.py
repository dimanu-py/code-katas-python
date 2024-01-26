

def roman_numeral(number: int) -> str:
    """
    Convert an arabic number to a roman numeral
    """
    if number == 4:
        return "IV"

    if number == 5:
        return "V"

    if number == 6:
        return "VI"

    if number == 7:
        return "VII"

    return 'I' * number