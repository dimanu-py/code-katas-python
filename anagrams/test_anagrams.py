from anagrams.anagrams import anagrams
import pytest


class TestAnagramsShould:

    def test_return_empty_list_when_no_word_is_given(self) -> None:
        assert anagrams("") == [""]

    @pytest.mark.parametrize(
        "word, expected",
        [
            ("a", ["a"]),
            ("b", ["b"]),
            ("ab", ["ab", "ba"]),
            ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
            ("biro", ["biro", "bior", "brio", "broi", "boir", "bori", "ibro", "ibor", "irbo", "irob", "iobr", "iorb", "rbio", "rboi", "ribo", "riob", "robi", "roib", "obir", "obri", "oibr", "oirb", "orbi", "orib"])]
    )
    def test_return_all_anagrams(self, word: str, expected: list[str]) -> None:
        assert anagrams(word) == expected
