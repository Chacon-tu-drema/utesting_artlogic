import pytest

from mars_rover.mars_rover import MarsRover


class TestMarsRover:
    @pytest.mark.parametrize(
        "command, location",
        [
            ("", "0:0:N"),
            ("R", "0:0:E"),
            ("RR", "0:0:S"),
            ("RRR", "0:0:W"),
            ("RRRR", "0:0:N"),
            ("L", "0:0:W"),
            ("LL", "0:0:S"),
            ("LLL", "0:0:E"),
            ("LLLL", "0:0:N"),
            ("M", "0:1:N"),
            ("MM", "0:2:N"),
            ("MMRMMLM", "2:3:N"),
            ("MMMMMMMMMM", "0:0:N"),
        ],
    )
    def test_rotations(self, command: str, location: str) -> None:
        assert MarsRover().execute(command) == location
