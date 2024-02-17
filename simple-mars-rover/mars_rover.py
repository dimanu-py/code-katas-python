from orientation import Orientation, North
from coordinates import Coordinates


class InvalidCommandError(Exception):
    """Exception raised when invalid command is passed to rover."""
    def __init__(self, command: str) -> None:
        self.message = f"Invalid command introduced: {command}"
        super().__init__(self.message)


class MarsRover:

    def __init__(self) -> None:
        self.coordinates: Coordinates = Coordinates(0, 0)
        self.orientation: Orientation = North()

    def execute(self, command: str) -> str:

        for move in command:
            self._execute_command(move)

        return f"{self.coordinates.x}:{self.coordinates.y}:{self.orientation}"

    def _execute_command(self, move: str) -> None:
        commands_map = {
            "M": self.move_forward,
            "R": self.rotate_right,
            "L": self.rotate_left
        }

        try:
            commands_map[move]()
        except KeyError:
            raise InvalidCommandError(move)

    def move_forward(self) -> None:
        """Move the rover one grid point in the current direction."""

        self.coordinates = self.orientation.forward(self.coordinates)

    def rotate_right(self) -> None:
        """Rotate the rover 90 degrees to the right."""

        self.orientation = self.orientation.right()

    def rotate_left(self) -> None:
        """Rotate the rover 90 degrees to the left."""

        self.orientation = self.orientation.left()
