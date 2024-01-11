from typing import List

from test_framework import generic_test
import itertools


def find_maximum_subarray_bf2(A):
    """
    Time: O(n^2)
    Space: O(1)
    """
    n = len(A)
    max_sum = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += A[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum 

def find_maximum_subarray_bf1(A):
    """
    Time: O(n^3)
    Space: O(1)
    """
    n = len(A)
    max_sum = 0
    for subarray_size in range(1, n+1):
        for start_idx in range(n):
            end_idx = start_idx + subarray_size
            if not end_idx > n:
                max_sum = max(max_sum, sum(A[start_idx:end_idx]))

    return max_sum
    
    
def find_maximum_subarray(A: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    max_sum = min_sum = 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(running_sum, min_sum) 
        max_sum = max(max_sum, running_sum-min_sum)
    return max_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
