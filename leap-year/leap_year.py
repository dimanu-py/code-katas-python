

def is_leap_year(year: int) -> bool:
    """
    Returns True if a year is leap, False otherwise

    A year is leap if is divisible by 4, and if is divisible by 100 and by 400.
    This means that a year is leap if is divisible by 4 and not by 100, or if is divisible by 400.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)