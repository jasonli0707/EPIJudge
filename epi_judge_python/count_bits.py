from test_framework import generic_test


def count_bits(x: int) -> int:
    """count the number of bits that are set to 1 in a positive integer

    Args:
        x (int): positive integer input

    Returns:
        int: number of bits that are set to 1
    """

    n = 0
    while x:
        n += x & 1
        x = x >> 1
    return n


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
