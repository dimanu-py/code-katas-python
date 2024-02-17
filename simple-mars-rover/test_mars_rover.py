import pytest

from mars_rover import MarsRover


class TestMarsRover:

    @pytest.fixture
    def rover(self) -> MarsRover:
        return MarsRover()

    def test_initial_position_is_0_0_N(self, rover: MarsRover):

        assert rover.x_coordinate == 0
        assert rover.y_coordinate == 0
        assert rover.facing == "N"

    def test_empty_command_does_not_move_rover(self, rover: MarsRover):

        position = rover.execute("")

        assert position == "0:0:N"

    @pytest.mark.parametrize(
        "command, expected_position",
        [("M", "0:1:N"), ("MM", "0:2:N"), ("MMMMMMMM", "0:8:N")]
    )
    def test_move_command_moves_rover_in_facing_direction(self, rover: MarsRover, command: str, expected_position: str) -> None:

        position = rover.execute(command)

        assert position == expected_position

    @pytest.mark.parametrize(
        "command, expected_position",
        [("R", "0:0:E"), ("RR", "0:0:S"), ("RRR", "0:0:W"), ("RRRR", "0:0:N")]
    )
    def test_right_command_rotates_rover_clockwise(self, rover: MarsRover, command: str, expected_position: str) -> None:

        position = rover.execute(command)

        assert position == expected_position

    @pytest.mark.parametrize(
        "command, expected_position",
        [("L", "0:0:W"), ("LL", "0:0:S"), ("LLL", "0:0:E"), ("LLLL", "0:0:N")]
    )
    def test_left_command_rotates_rover_counter_clockwise(self, rover: MarsRover, command: str, expected_position: str) -> None:

        position = rover.execute(command)

        assert position == expected_position
