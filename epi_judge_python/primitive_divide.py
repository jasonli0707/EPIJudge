from test_framework import generic_test


def divide(x: int, y: int) -> int:
    """compute quotient of two positive integers using only addition, subtraction and shifting operators

    Args:
        x (int): positive integer
        y (int): positive integer

    Returns:
        int: quotient x/y
    """

    quotient, k = 0, 32
    yk = y << k # 2^k * y
    while x >= y: # until remainder smaller than y
        while x < yk: # find the largest k wher 2^k * y < x
            yk >>= 1
            k -= 1
        x -= yk # remainder
        quotient += (1<<k) # add 2^k

    return quotient


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
