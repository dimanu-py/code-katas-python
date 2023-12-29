

def is_leap_year(year: int) -> bool:
    """
    Returns True if a year is leap, False otherwise

    A year is leap if is divisible by 4, and if is divisible by 100 and by 400.
    This means that a year is leap if is divisible by 4 and not by 100, or if is divisible by 400.
    """
    return year_divisible_by(4, year) and (year_not_divisible_by(100, year) or year_divisible_by(400, year))


def year_divisible_by(number: int, year: int) -> bool:
    return year % number == 0


def year_not_divisible_by(number: int, year: int) -> bool:
    return year % number != 0