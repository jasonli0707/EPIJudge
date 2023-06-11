from test_framework import generic_test
from collections import Counter


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    """
    Time: O(n+m)
    Space: O(L) i.e. L is the number of distinct characters in the letter
    """
    letter_counts = Counter(letter_text)

    for c in magazine_text:
        if c in letter_counts:
            letter_counts[c] -= 1
            if letter_counts[c] == 0:
                del letter_counts[c]
                if not letter_counts: # already empty i.e. covered
                    return True

    return not letter_counts  # every character in letter_text is covered by the magazine

def pythonic_sol(letter_text, magazine_text):
    # only keep postive counts. If counts == 0, then key will be removed
    return not (Counter(letter_text) - Counter(magazine_text))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
