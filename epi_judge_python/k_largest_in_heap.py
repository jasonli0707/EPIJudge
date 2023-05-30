from typing import List
import heapq

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    """return k largest elements in a max heap
    Time: O(klogk)
    Space: O(k)
    """
    if k < 1:
        return []

    result = []
    max_candidates = []

    heapq.heappush(max_candidates, (-A[0], 0)) # push largest element and its index

    for _ in range(k):
        value, idx = heapq.heappop(max_candidates)
        result.append(-value)

        # left and right child in a heap
        left = idx*2 + 1
        if left < len(A):
            heapq.heappush(max_candidates, (-A[left], left))

        right = idx*2 + 2 
        if right < len(A):
            heapq.heappush(max_candidates, (-A[right], right))
        
        
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
