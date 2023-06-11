from test_framework import generic_test
from collections import Counter


def can_form_palindrome(s: str) -> bool:
    """
    Time: O(n)
    Space: O(c) i.e. c is the number of distinct characters
    """
    return sum(v%2 for v in Counter(s).values()) <= 1 # if v is odd, then add 1 to the final result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
