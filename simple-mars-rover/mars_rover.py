from orientation import Orientation, North


class InvalidCommandError(Exception):
    """Exception raised when invalid command is passed to rover."""
    def __init__(self, command: str) -> None:
        self.message = f"Invalid command introduced: {command}"
        super().__init__(self.message)


class MarsRover:

    def __init__(self) -> None:
        self.x_coordinate: int = 0
        self.y_coordinate: int = 0
        self.orientation: Orientation = North()

    def execute(self, command: str) -> str:

        for move in command:
            self._execute_command(move)

        return f"{self.x_coordinate}:{self.y_coordinate}:{self.facing}"

    def _execute_command(self, move: str) -> None:
        commands_map = {
            "M": self.move_straight,
            "R": self.rotate_right,
            "L": self.rotate_left
        }

        try:
            commands_map[move]()
        except KeyError:
            raise InvalidCommandError(move)

    def move_straight(self) -> None:
        if self.facing == "N":
            self.y_coordinate = self.y_coordinate + 1 if self.y_coordinate < 9 else 0
        elif self.facing == "E":
            self.x_coordinate = self.x_coordinate + 1 if self.x_coordinate < 9 else 0
        elif self.facing == "S":
            self.y_coordinate = self.y_coordinate - 1 if self.y_coordinate > 0 else 9
        elif self.facing == "W":
            self.x_coordinate = self.x_coordinate - 1 if self.x_coordinate > 0 else 9

    def rotate_right(self) -> None:
        """Rotate the rover 90 degrees to the right."""

        right_rotation_transitions = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }
        self.facing = right_rotation_transitions[self.facing]

    def rotate_left(self) -> None:
        """Rotate the rover 90 degrees to the left."""

        left_rotation_transitions = {
            "N": "W",
            "W": "S",
            "S": "E",
            "E": "N"
        }
        self.facing = left_rotation_transitions[self.facing]
