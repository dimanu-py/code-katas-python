

def roman_numeral(number: int) -> str:
    """
    Convert an arabic number to a roman numeral
    """

    if number <= 0 or number >= 4000:
        raise ValueError("Number must be between 1 and 3999")

    number_conversion = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    roman_number = ""

    for arabic, roman in number_conversion.items():
        while number >= arabic:
            roman_number += roman
            number -= arabic

    return roman_number
