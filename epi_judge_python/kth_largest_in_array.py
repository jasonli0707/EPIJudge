from typing import List

from test_framework import generic_test
import random


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    """
    Quick select
    Time: average O(n) , worst-case: O(n^2)
    Space: O(1)
    """

    def quick_select(left, right):
        pivot_idx = random.randint(left, right)
        A[right], A[pivot_idx] = A[pivot_idx], A[right] # swap pivot element to the end of the array
        pivot_idx = left
        for i in range(left, right): # compare every element to the pivot
            if A[i] > A[right]: # move elements larger than pivot to the left
                A[i], A[pivot_idx] = A[pivot_idx], A[i]
                pivot_idx += 1
    
        A[right], A[pivot_idx] = A[pivot_idx], A[right] # swap the pivot element back to the pivot index
        return pivot_idx
        
    left, right = 0, len(A)-1

    while left<=right:
        new_pivot_idx = quick_select(left, right)
        if new_pivot_idx == k-1:
            return A[new_pivot_idx]
        elif new_pivot_idx > k-1: # more than k-1 elements larger than the pivot
            right = new_pivot_idx - 1
        else:
            left = new_pivot_idx + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
