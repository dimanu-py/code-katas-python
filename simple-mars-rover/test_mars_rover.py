import pytest

from mars_rover import MarsRover, InvalidCommandError


class TestMarsRover:

    @pytest.fixture
    def rover(self) -> MarsRover:
        return MarsRover()

    def test_initial_position_is_0_0_N(self, rover: MarsRover):

        position = f"{rover.x_coordinate}:{rover.y_coordinate}:{rover.orientation}"
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
        [("R", "0:0:E"), ("RR", "0:0:S"), ("RRR", "0:0:W"), ("RRRR", "0:0:N"),
         ("L", "0:0:W"), ("LL", "0:0:S"), ("LLL", "0:0:E"), ("LLLL", "0:0:N")]
    )
    def test_rotate_command_modifies_facing_direction(self, rover: MarsRover, command: str, expected_position: str) -> None:

        position = rover.execute(command)

        assert position == expected_position

    @pytest.mark.parametrize(
        "command, expected_position",
        [("RM", "1:0:E"), ("RMM", "2:0:E"), ("MRRM", "0:0:S"), ("MMMRMMRM", "2:2:S"), ("MRMLLM", "0:1:W"), ("MMRMMLM", "2:3:N")]
    )
    def test_rotate_and_move_correctly(self, rover: MarsRover, command: str, expected_position: str) -> None:

        position = rover.execute(command)

        assert position == expected_position

    @pytest.mark.parametrize(
        "command, expected_position",
        [("M" * 10, "0:0:N"), ("R" + "M" * 10, "0:0:E"), ("LMM", "8:0:W"), ("LLM", "0:9:S")]
    )
    def test_when_rover_goes_outside_grid_it_wrap_around(self, rover: MarsRover, command: str, expected_position: str) -> None:

        position = rover.execute(command)

        assert position == expected_position

    @pytest.mark.parametrize("command", ["MMMMX", "AA", "RMMLMY"])
    def test_invalid_command_can_not_be_executed(self, rover: MarsRover, command: str) -> None:

        with pytest.raises(InvalidCommandError):
            rover.execute(command)
