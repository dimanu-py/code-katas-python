from roman_numerals import roman_numeral


class TestRomanNumeralShould:

    def test_convert_1_to_I(self) -> None:
        assert roman_numeral(1) == 'I'

    def test_convert_2_to_II(self) -> None:
        assert roman_numeral(2) == 'II'