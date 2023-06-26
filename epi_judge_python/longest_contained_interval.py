from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    """
    Time: O(n)
    """

    hash_table = set(A)
    max_range = 0
    
    while hash_table:
        a = hash_table.pop()

        lower = a - 1
        while lower in hash_table:
            hash_table.remove(lower)
            lower -= 1

        upper = a + 1
        while upper in hash_table:
            hash_table.remove(upper)
            upper += 1

        max_range = max(max_range, upper-lower-1)

    return max_range


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
