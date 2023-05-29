from typing import Iterator, List
import heapq
from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    """
    Time: O(logn)
    Space: O(n)
    """
    min_heap = [] # store higher-half
    max_heap = [] # store lower-half
    result = []

    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))

        if len(max_heap) > len(min_heap): # ensure min_heap has the same or one more element than max_heap
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        
        result.append(0.5*(min_heap[0]+ -max_heap[0]) if len(max_heap) == len(min_heap) else min_heap[0])

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
