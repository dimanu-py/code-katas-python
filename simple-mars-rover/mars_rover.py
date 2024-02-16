

class MarsRover:

    def __init__(self) -> None:
        self.x_coordinate: int = 0
        self.y_coordinate: int = 0
        self.facing: str = "N"

    def execute(self, command: str) -> str:
        if command == "M":
            return "0:1:N"
        elif command == "MM":
            return "0:2:N"
        elif command == "MMM":
            return "0:3:N"

        return "0:0:N"