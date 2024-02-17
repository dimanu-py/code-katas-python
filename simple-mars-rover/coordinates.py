

class Coordinates:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

        if self.x < 0:
            self.x = 9

        if self.y < 0:
            self.y = 9

        if self.x > 9:
            self.x = 0

        if self.y > 9:
            self.y = 0
