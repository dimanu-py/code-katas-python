

class MarsRover:

    def __init__(self) -> None:
        self.x_coordinate: int = 0
        self.y_coordinate: int = 0
        self.facing: str = "N"

    def execute(self, command: str) -> str:

        if command == "":
            return f"{self.x_coordinate}:{self.y_coordinate}:{self.facing}"

        for move in command:
            if move == "M":
                self.y_coordinate += 1
            elif move == "R":
                self.rotate_right()
            elif move == "L":
                self.rotate_left()

        return f"0:{self.y_coordinate}:{self.facing}"

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
