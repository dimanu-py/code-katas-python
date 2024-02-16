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