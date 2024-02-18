from abc import ABC, abstractmethod

from mars_rover import MarsRover


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        """Execute the command."""


class MoveForward(Command):
    """Move the rover one grid point in the current direction."""

    def __init__(self, rover: MarsRover) -> None:
        self.rover = rover

    def execute(self) -> None:
        self.rover.move_forward()