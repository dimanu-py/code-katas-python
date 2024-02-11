

def roman_numeral(number: int) -> str:
    """
    Convert an arabic number to a roman numeral
    """
    if number == 4:
        return "IV"

    result = ""
    if number >= 5:
        result = "V"
        number -= 5

    return result + "I" * number
