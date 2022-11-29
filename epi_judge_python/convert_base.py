from test_framework import generic_test
import functools


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    '''
    Time: O(n)
    Space: O(n)
    e.g. ('615', 7, 13) -> 615 in base 7 = 1A7 in base 13 where [10, ..., 15] is represented by [A, ..., F]
    '''
    is_negative = (num_as_string[0] == '-')
    hexdigits = '0123456789ABCDEF'

    # base b1 to decimal
    dec = functools.reduce(lambda running_sum, c: running_sum*b1 + hexdigits.index(c), num_as_string[is_negative:], 0)
    if dec == 0: return "0"


    # decimal to base b2
    s = []
    while dec:
        remainder = dec%b2
        dec //= b2 
        s.append(hexdigits[remainder]) 

    if is_negative:
        s.append('-')
        
    return ''.join(reversed(s))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
