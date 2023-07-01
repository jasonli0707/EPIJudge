from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    """
    Time: O(n+m)
    """
    if not A or not B: # if either one is empty
        return []
 
    result = []
    n, m = len(A), len(B)
    i = j = 0
    while  i < n and j < m:
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            common = A[i]
            result.append(common)
            while i < n and A[i] == common:
                i += 1
            while j < m and B[j] == common:
                j += 1

    return result 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
