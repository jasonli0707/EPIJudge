from typing import List

from test_framework import generic_test


def min_jump(nums: List[int]) -> int:
    '''
    return the minimun number of jumps to reach the last index
    Greedy sol: O(n) Time, O(1) Space
    '''
    n = len(nums)
    if n == 1: return 0
    l=r=res=0
    
    while r < n-1:
        furthest = 0
        for i in range(l, r+1):
            furthest = max(nums[i] + i, furthest)
        l = r + 1
        r = furthest
        res += 1
            
    return res
      

def can_jump(nums: List[int]) -> bool:
    '''O(1) Space
       O(n) Time'''
    n = len(nums)
    last_idx = n-1
    for i in range(n-2, -1, -1):
        if i + nums[i] >= last_idx:
            last_idx = i
        
    return last_idx == 0

def can_reach_end(A: List[int]) -> bool:
    """determine whether it is possible to advance to the last index of the list in A
       Time: O(n)
       Space: O(1)
    Args:
        A (List[int]): an array with n integers, A[i] denotes the maximum steps you can advance from index i
    Returns:
        bool: whether it is able to reach the last index
    """

    furthest_range = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_range and furthest_range < last_idx:
        furthest_range = max(furthest_range, A[i] + i) # robust to negative entries
        i += 1

    return furthest_range >= last_idx # true if furthest range reached covers the last index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
