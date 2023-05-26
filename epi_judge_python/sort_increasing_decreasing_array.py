from typing import List
import heapq

from test_framework import generic_test


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    """sort an array with k-increasing-decreasing property e.g. 2-increasing-decreasing [1, 4, 3, 2, 5, 1]
       Time: O(nlogk)
       Space: O(k)
    """

    # decompose array A into multiple sorted arrays
    sorted_arrays = []
    start_idx = 0
    is_increasing = True
    for i in range(1, len(A)):
        if is_increasing and A[i] < A[i-1]:
            is_increasing = False
            sorted_arrays.append(A[start_idx:i]) # from start_idx to i-1
            start_idx = i
        elif not is_increasing and A[i] > A[i-1]:
            is_increasing = True
            sorted_arrays.append(A[i-1:start_idx-1:-1]) # from i-1 to start_idx
            start_idx = i

    i += 1 # including last element
    sorted_arrays.append(A[start_idx:i] if is_increasing else A[i-1:start_idx-1:-1]) # add last subarray
 
    # heap-merge sorted arrays
    result = []  
    min_heap = []

    sorted_iters = [iter(arr) for arr in sorted_arrays]

    for i, it in enumerate(sorted_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    while min_heap:
        smallest_val, iter_idx = heapq.heappop(min_heap)
        result.append(smallest_val)
        next_val = next(sorted_iters[iter_idx], None)
        if next_val is not None:
           heapq.heappush(min_heap, (next_val, iter_idx))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
