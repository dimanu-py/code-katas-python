from roman_numerals import roman_numeral
import pytest


class TestRomanNumeralShould:

    @pytest.mark.parametrize(
        "number, expected",
        [(1, "I"), (2, "II"), (3, "III"), (4, "IV"), (5, "V"), (6, "VI"), (7, "VII"), (8, "VIII"), (9, "IX"),
         (10, "X"), (11, "XI")]
    )
    def test_convert_number_to_numeral(self, number: int, expected: str) -> None:

        numeral = roman_numeral(number)

        assert numeral == expected
