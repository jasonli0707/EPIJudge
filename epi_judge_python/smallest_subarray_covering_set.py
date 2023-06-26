import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    """
    Time: O(n) size of paragraph
    Space: O(m) size of keywords
    """

    target = collections.Counter(keywords) 
    remaining = sum(target.values())
    result = Subarray(-1, -1)

    start = 0
    min_len = len(paragraph) + 1

    for end, word in enumerate(paragraph): # move the right pointer until a valid subarray is found
        if word in target:
            target[word] -= 1
            if target[word] >= 0:
                remaining -= 1

        while not remaining: # valid subarray covering all words in keywords
            if end - start < min_len: # if current subarray is the smallest, update the result
                result = Subarray(start, end)
                min_len = end - start
            start_word = paragraph[start]
            if start_word in keywords: 
                target[start_word] += 1
                if target[start_word] > 0:
                    remaining += 1
            start += 1 # move the left pointer until the subarray is no longer valid

    return result


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
