

class MarsRover:

    def __init__(self) -> None:
        self.x_coordinate: int = 0
        self.y_coordinate: int = 0
        self.facing: str = "N"

    def execute(self, command: str) -> str:

        if command == "":
            return "0:0:N"

        for move in command:
            if move == "M":
                self.y_coordinate += 1
            elif move == "R":
                self.facing = "E"

        return f"0:{self.y_coordinate}:{self.facing}"