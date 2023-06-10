from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure
import itertools


def find_missing_element(stream: Iterator[int]) -> int:
    NUM_BUCKET = 1 << 16 # 2^16
    counter = [0] * NUM_BUCKET # 2^16 uint16 = 128 KB
    stream, stream_copy = itertools.tee(stream)
    for x in stream:
        upper_part_x = x >> 16 # extract 16 MSBs
        counter[upper_part_x] += 1
   
    # look for a bucket that contains less than 1 << 16 i.e 2^16 elements
    BUCKET_CAPACITY = 1 << 16
    candidate_bucket = next(i for i, c in enumerate(counter) if c < BUCKET_CAPACITY) # a single missing candidate

    # Find all IP addresses in the stream whose first 16 bits are equal to candidate_bucket
    candidates = [0] * BUCKET_CAPACITY
    stream = stream_copy
    for x in stream_copy:
        upper_part_x = x >> 16
        if upper_part_x == candidate_bucket: # if MSBs match, then record LSBs
            lower_part_x = ((1<<16) - 1) & x
            candidates[lower_part_x] += 1

    # iterate all possible LSBs to find the missing one
    for i, v in enumerate(candidates):
        if v == 0: # absent LSBs
            return (candidate_bucket << 16) | i
            
    return -1

def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
