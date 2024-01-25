from anagrams.anagrams import anagrams
import pytest


class TestAnagramsShould:

    def test_return_empty_list_when_no_word_is_given(self) -> None:
        assert anagrams("") == [""]

    @pytest.mark.parametrize("word", ["a", "b", "c"])
    def test_return_same_word_when_only_has_one_syllable(self, word: str) -> None:
        assert anagrams(word) == [word]