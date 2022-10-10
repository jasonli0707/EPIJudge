from test_framework import generic_test

def brute_force(x):
    sign = 1
    if x < 0:
        sign = -1
        x*=sign

    return int(str(x)[::-1])*sign

def reverse(x: int) -> int:
    """reverse the digits in x without changing the sign e.g. 24 -> 42, -14 -> -41
       without directly casting to str
       Time Complexity: O(n)
    Args:
        x (int): n digits integer

    Returns:
        int: x with reversed digits
    """
    result = 0
    x_remaining = abs(x)
    while x_remaining:
        result = 10*result + x_remaining%10
        x_remaining //= 10
 
    return result if x > 0 else -result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
