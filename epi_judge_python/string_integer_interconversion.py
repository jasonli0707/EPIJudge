from test_framework import generic_test
from test_framework.test_failure import TestFailure
import functools
import string

def int_to_string(x: int) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    s = [] # mutable list
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    while True:
        # ord() get integer representation from ascii table
        # x%10 extracts least significant digit
        s.append(chr(ord('0') + x%10)) 
        x//=10
        if x == 0:
            break

    if is_negative:
       s.append('-') 

    return ''.join(reversed(s)) # immutable string


def string_to_int(s: str) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    # The function in functools.reduce() takes two arguments (1) cumulative result (2) next element from list and applies iteratively to the list
    return functools.reduce(lambda running_sum, c: 10*running_sum + string.digits.index(c), s[(s[0]== '-' or s[0] == '+'):], 0) * (-1 if s[0]=='-' else 1)

def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
