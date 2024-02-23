

def anagrams(word: str) -> list[str]:
    """
    Return a list of all the possible anagrams of a word.
    """
    if len(word) <= 1:
        return [word]

    anagrams_results = []
    for index, fixed_letter in enumerate(word):
        for anagram in anagrams(word[:index] + word[index + 1:]):
            anagrams_results.append(fixed_letter + anagram)

    return anagrams_results