import pytest

from mars_rover import MarsRover


class TestMarsRover:

    def test_initial_position_is_0_0_N(self):
        rover = MarsRover()

        assert rover.x_coordinate == 0
        assert rover.y_coordinate == 0
        assert rover.facing == "N"

    def test_empty_command_does_not_move_rover(self):
        rover = MarsRover()

        position = rover.execute("")

        assert position == "0:0:N"

    @pytest.mark.parametrize(
        "command, expected_position",
        [("M", "0:1:N"), ("MM", "0:2:N"), ("MMMMMMMM", "0:8:N")]
    )
    def test_move_command_moves_rover_in_facing_direction(self, command: str, expected_position: str) -> None:
        rover = MarsRover()

        position = rover.execute(command)

        assert position == expected_position

    def test_right_command_rotates_rover_clockwise(self) -> None:
        rover = MarsRover()

        rover.execute("R")

        assert rover.facing == "E"

