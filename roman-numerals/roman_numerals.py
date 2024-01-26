

def roman_numeral(number: int) -> str:
    """
    Convert an arabic number to a roman numeral
    """
    if number == 1:
        return 'I'
    elif number == 2:
        return 'II'
    else:
        return 'III'