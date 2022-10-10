from test_framework import generic_test
import math


def reverse(x):
    result = 0
    x_remains = abs(x)
    while x_remains:
        result = 10*result + x_remains%10
        x_remains //= 10

    return result if x > 0 else -result

def brute_force(x):
    if x<0:
        return False
    return x == reverse(x)
    

def is_palindrome_number(x: int) -> bool:
    """check if the integer's representation as a decimal string is a palindrome e.g. 123 -> False, 4224 -> True, -1 -> False
       Time Complexity: O(n)
       Space Complexity: O(1)
    Args:
        x (int): integer

    Returns:
        bool: whether x is a palindrome number
    """
    if x <= 0:
        return x==0
    n_digits = math.floor(math.log10(x)) + 1 # log(0) raises ValueError: math domain error
    msd_mask = pow(10, n_digits-1)
    for _ in range(n_digits//2): # two pointer technique
        lsd = x%10
        if lsd != x//msd_mask:
            return False
        x %= msd_mask # remove msd
        x //=10 # remove lsd
        msd_mask //= 100 # handle leading zero e.g. 069
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
