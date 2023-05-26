import heapq
from typing import List
from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    """merge sorted arrays using heap
    Time: O(nlogk), n elements each takes O(logk) for heappushpop
    Space: O(k) additional storage for maintaining the min heap
    """

    min_heap = []
    result = []

    sorted_iters = [iter(arr) for arr in sorted_arrays]

    # initialize a heap using the first element from each array
    for i, it in enumerate(sorted_iters):
        first_element = next(it, None)
        if first_element is not None: # get rid of empty array
            heapq.heappush(min_heap, (first_element, i))


    while min_heap:
        smallest_val, iter_idx = heapq.heappop(min_heap)
        result.append(smallest_val)
        next_val = next(sorted_iters[iter_idx], None)
        if next_val is not None: 
            heapq.heappush(min_heap, (next_val, iter_idx))

    return result
    
def merge_sorted_arrays_pythonic(sorted_arrays: List[List[int]]) -> List[int]:
    return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
