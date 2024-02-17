from abc import ABC, abstractmethod


class Orientation(ABC):
    """Class to represent where the rover is facing and how it moves."""

    @abstractmethod
    def right(self, ) -> None:
        """Rotate the rover 90 degrees to the right."""

    @abstractmethod
    def left(self, ) -> None:
        """Rotate the rover 90 degrees to the left."""