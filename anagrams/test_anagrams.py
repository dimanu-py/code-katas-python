from anagrams.anagrams import anagrams


class TestAnagramsShould:

    def test_return_empty_list_when_no_word_is_given(self):
        assert anagrams("") == [""]