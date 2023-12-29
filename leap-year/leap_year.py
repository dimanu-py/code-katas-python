

class Year:
    def __init__(self, year: int) -> None:
        self.year = year

    def is_leap(self) -> bool:
        """
        Returns True if a year is leap, False otherwise

        A year is leap if is divisible by 4, and if is divisible by 100 and by 400.
        This means that a year is leap if is divisible by 4 and not by 100, or if is divisible by 400.
        """
        return self.divisible_by(4) and (self.not_divisible_by(100) or self.divisible_by(400))

    def divisible_by(self, number: int) -> bool:
        return self.year % number == 0

    def not_divisible_by(self, number: int) -> bool:
        return self.year % number != 0