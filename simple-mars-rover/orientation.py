from abc import ABC, abstractmethod


class Orientation(ABC):
    """Class to represent where the rover is facing and how it moves."""

    @abstractmethod
    def right(self, ) -> "Orientation":
        """Rotate the rover 90 degrees to the right."""

    @abstractmethod
    def left(self, ) -> "Orientation":
        """Rotate the rover 90 degrees to the left."""


class North(Orientation):
    """Class to represent the rover facing North."""

    def right(self) -> "Orientation":

        return East()

    def left(self) -> "Orientation":

        return West()


class East(Orientation):
    """Class to represent the rover facing East."""

    def right(self) -> "Orientation":

        return South()

    def left(self) -> "Orientation":

        return North()