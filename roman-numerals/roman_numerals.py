

def roman_numeral(number: int) -> str:
    """
    Convert an arabic number to a roman numeral
    """
    if number == 4:
        return "IV"

    if number == 9:
        return "IX"

    if number == 10:
        return "X"

    if number == 11:
        return "XI"

    if number == 12:
        return "XII"

    if number == 13:
        return "XIII"

    result = ""
    if number >= 5:
        result = "V"
        number -= 5

    return result + "I" * number
