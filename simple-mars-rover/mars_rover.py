

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
                if self.facing == "N":
                    self.facing = "E"
                elif self.facing == "E":
                    self.facing = "S"

        return f"0:{self.y_coordinate}:{self.facing}"