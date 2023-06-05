import collections
from typing import List
from math import inf

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A: List[int]) -> MinMax:
    """
    Time: O(n)
    Space: O(1)
    """

    if len(A) == 1:
        return MinMax(A[0], A[0])

    result = MinMax(inf, -inf) # initialise

    for i in range(0, len(A)-1, 2):
        current_min, current_max = (A[i+1], A[i]) if A[i] > A[i+1] else (A[i], A[i+1])
        result = MinMax(min(current_min, result.smallest), max(current_max, result.largest))

    if len(A) % 2: # if odd number of elements, also compare the last element
        result = MinMax(min(A[-1], result.smallest), max(A[-1], result.largest))
    
    return result

def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
