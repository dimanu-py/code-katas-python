from abc import ABC, abstractmethod
from coordinates import Coordinates


class Orientation(ABC):
    """Class to represent where the rover is facing and how it moves."""

    @abstractmethod
    def right(self, ) -> "Orientation":
        """Rotate the rover 90 degrees to the right."""

    @abstractmethod
    def left(self, ) -> "Orientation":
        """Rotate the rover 90 degrees to the left."""

    @abstractmethod
    def forward(self, current_coordinates: Coordinates) -> Coordinates:
        """Move the rover forward in the facing direction."""


class North(Orientation):
    """Class to represent the rover facing North."""

    def __repr__(self) -> str:
        return "N"

    def right(self) -> "Orientation":

        return East()

    def left(self) -> "Orientation":

        return West()

    def forward(self, current_coordinates: Coordinates) -> Coordinates:

        y_increment = 1
        return Coordinates(current_coordinates.x, current_coordinates.y + y_increment)


class East(Orientation):
    """Class to represent the rover facing East."""

    def __repr__(self) -> str:
        return "E"

    def right(self) -> "Orientation":

        return South()

    def left(self) -> "Orientation":

        return North()

    def forward(self, current_coordinates: Coordinates) -> Coordinates:

        x_increment = 1
        return Coordinates(current_coordinates.x + x_increment, current_coordinates.y)


class South(Orientation):
    """Class to represent the rover facing South."""

    def __repr__(self) -> str:
        return "S"

    def right(self) -> "Orientation":

        return West()

    def left(self) -> "Orientation":

        return East()

    def forward(self, current_coordinates: Coordinates) -> Coordinates:

        y_increment = -1
        return Coordinates(current_coordinates.x, current_coordinates.y + y_increment)



class West(Orientation):
    """Class to represent the rover facing West."""

    def __repr__(self) -> str:
        return "W"

    def right(self) -> "Orientation":

        return North()

    def left(self) -> "Orientation":

        return South()

    def forward(self, current_coordinates: Coordinates) -> Coordinates:

        x_increment = -1
        return Coordinates(current_coordinates.x + x_increment, current_coordinates.y)
