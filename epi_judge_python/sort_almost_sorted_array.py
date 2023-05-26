from typing import Iterator, List
from itertools import islice
import heapq

from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int], k: int) -> List[int]:
    """_summary_

    Args:
        sequence (Iterator[int]): a k-sorted list
        k (int): an element is at most k away from its final sorted position

    Returns:
        List[int]: sorted list
    """
    min_heap = []  # keep track of k + 1 elements
    result = []

    for item in islice(sequence, k):
        heapq.heappush(min_heap, item)


    for item in sequence: # will start from the (k + 1)th element
        result.append(heapq.heappushpop(min_heap, item))

    while min_heap:
       result.append(heapq.heappop(min_heap)) 

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
