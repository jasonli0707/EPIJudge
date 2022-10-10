from re import L
from unittest import result
from test_framework import generic_test

def count_bits(x):
    counts = 0
    while x:
        counts += (x&1)
        x = x >> 1
    return counts

def brute_force(x: int) -> int:
    """try all nearest integers i.e. x-1, x+1, x-2, x+2, ...
        Worst case: x = 2^n => Time complexity: O(2^(n-1))
    """
    offset = 1
    weight = count_bits(x)
    while True:
        positive = x + offset
        if weight == count_bits(positive):
            return positive
        negative = x - offset
        if weight == count_bits(negative):
            return negative
        offset += 1

def linear_time_sol(x):
    """swap the two rightmost consecutive bits that differ using linear scan
       Time complexity: O(n)
    """
    NUM_UNSIGNED_BIT = 64
    for i in range(64):
        if ((x >> i) & 1) != ((x >> (i+1)) & 1):
            x ^= (1 << i )| (1 << (i + 1))
            return x
    raise ValueError('All bit are 0 or 1')


def constant_time_sol(x):
    """
        directly swap the two rightmost consecutive bits that differ with bit operations
        Time Complexity: O(1)
    """
    lowest_bit_set = (x & ~(x-1))
    lowest_bit_not_set = (~x & (x+1))
    if (lowest_bit_not_set>lowest_bit_set):
        x|=lowest_bit_not_set
        x^=lowest_bit_not_set>>1
    else:
        x^=lowest_bit_set
        x|=lowest_bit_set>>1
    return x

def closest_int_same_bit_count(x: int) -> int:
    """
    Args:
        x (int): 64-bit nonnegative integer

    Returns:
        int: closest integer to x with same number of bits set to 1
    """

    lowest_bit_set = (x & ~(x-1))
    lowest_bit_not_set = (~x & (x+1))
    if (lowest_bit_not_set>lowest_bit_set):
        x|=lowest_bit_not_set
        x^=lowest_bit_not_set>>1
    else:
        x^=lowest_bit_set
        x|=lowest_bit_set>>1
    return x




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
