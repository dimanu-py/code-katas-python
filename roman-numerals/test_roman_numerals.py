from roman_numerals import roman_numeral
import pytest


class TestRomanNumeralShould:

    @pytest.mark.parametrize(
        "number, expected",
        [(1, "I"), (2, "II"), (3, "III"), (4, "IV"), (5, "V"), (6, "VI"), (7, "VII"), (8, "VIII"), (9, "IX"),
         (10, "X"), (11, "XI"), (12, "XII"), (13, "XIII"), (14, "XIV"), (15, "XV"), (16, "XVI"), (17, "XVII"), (18, "XVIII"),
         (19, "XIX"), (20, "XX"), (21, "XXI"), (22, "XXII"), (23, "XXIII"), (24, "XXIV"), (25, "XXV"), (26, "XXVI"), (27, "XXVII"),
         (30, "XXX"), (40, "XL"), (50, "L"), (60, "LX"), (70, "LXX"), (80, "LXXX"), (90, "XC"), (100, "C"), (200, "CC"), (300, "CCC"),
         (400, "CD"), (500, "D"), (600, "DC"), (700, "DCC"), (800, "DCCC"), (900, "CM"), (1000, "M"), (846, "DCCCXLVI"),
         (1999, "MCMXCIX"), (2008, "MMVIII"), (3999, "MMMCMXCIX")]
    )
    def test_convert_number_to_numeral(self, number: int, expected: str) -> None:

        numeral = roman_numeral(number)

        assert numeral == expected

    @pytest.mark.parametrize("number", [0, -1, -10, 4000])
    def test_invalid_arabic_numeral_raise_error(self, number: int) -> None:

        with pytest.raises(ValueError):
            roman_numeral(number)