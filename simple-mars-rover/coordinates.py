

class Coordinates:

    def __init__(self, x: int, y: int) -> None:
        self.x = self._wrap_around(x)
        self.y = self._wrap_around(y)

    @staticmethod
    def _wrap_around(coordinate: int) -> int:
        """
        Wrap around the grid when the rover goes outside the grid.

        This is, when the rover goes outside the grid, it will appear on the opposite side.
        For example, if the rover goes outside the grid at the top, it will appear at the bottom.
        """
        return coordinate % 10