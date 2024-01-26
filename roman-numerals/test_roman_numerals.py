from roman_numerals import roman_numeral


class TestRomanNumeralShould:

    def test_convert_1_to_I(self) -> None:
        assert roman_numeral(1) == 'I'
