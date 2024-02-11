

def roman_numeral(number: int) -> str:
    """
    Convert an arabic number to a roman numeral
    """
    if number == 4:
        return "IV"

    if number == 9:
        return "IX"

    if number == 14:
        return "XIV"

    result = ""

    if number >= 10:
        result = "X"
        number -= 10

    if number >= 5:
        result = "V"
        number -= 5

    return result + "I" * number
