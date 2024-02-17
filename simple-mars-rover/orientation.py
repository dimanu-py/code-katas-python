from abc import ABC, abstractmethod


class Orientation(ABC):
    """Class to represent where the rover is facing and how it moves."""

    @abstractmethod
    def right(self, ) -> "Orientation":
        """Rotate the rover 90 degrees to the right."""

    @abstractmethod
    def left(self, ) -> "Orientation":
        """Rotate the rover 90 degrees to the left."""

    @abstractmethod
    def forward(self, x: int, y: int) -> (int, int):
        """Move the rover forward in the facing direction."""


class North(Orientation):
    """Class to represent the rover facing North."""

    def right(self) -> "Orientation":

        return East()

    def left(self) -> "Orientation":

        return West()

    def __repr__(self) -> str:
        return "N"



class East(Orientation):
    """Class to represent the rover facing East."""

    def right(self) -> "Orientation":

        return South()

    def left(self) -> "Orientation":

        return North()

    def __repr__(self) -> str:
        return "E"


class South(Orientation):
    """Class to represent the rover facing South."""

    def right(self) -> "Orientation":

        return West()

    def left(self) -> "Orientation":

        return East()

    def __repr__(self) -> str:
        return "S"


class West(Orientation):
    """Class to represent the rover facing West."""

    def right(self) -> "Orientation":

        return North()

    def left(self) -> "Orientation":

        return South()

    def __repr__(self) -> str:
        return "W"