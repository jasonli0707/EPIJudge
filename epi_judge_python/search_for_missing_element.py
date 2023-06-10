import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    """
    Time: O(n)
    Space: O(1)
    """

    i = 0
    while i < len(A):
        val = A[i]
        if val == i or A[val] == val:
            i += 1
        else:
            A[i], A[val] = A[val], A[i] 

    for i, x in enumerate(A):
        if i != x:
            return DuplicateAndMissing(x, i)
 
def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
