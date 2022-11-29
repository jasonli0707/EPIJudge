import functools
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

import random

def brute_force(n, k):
    '''
    Iteratively generate random int from [0, n-1] until get k distinct values
    Time: O(k)
    Space: O(n)
    '''
    A = list(range(n))
    for i in range(k):
        r = random.randint(i, n-1)
        A[r], A[i] = A[i], A[r]
    
    return A[:k]

def random_subset(n: int, k: int) -> List[int]:
    '''
    Use hashtable to record the swapping in the brute force algorithm
    Time: O(k)
    Space: O(k) # benefit if k<<n
    e.g. arr=[0, 1, 2, 3, 4, 5]
    h = {}
    For i=0 to 2:
    1st: i=0, r=2, arr[0]<=>arr[2], {(0,2) | (2,0)}
    2nd: i=1, r=2, arr[1]<=>arr[2], {(0,2), (1,0) | (2,1)}
    3rd: i=2, r=5, arr[2]<=>arr[5], {(0,2), (1,0) (2,5) | (5,1)}
    return [2, 0, 5]
    '''
    history = {}
    for i in range(k):
        rand_idx  = random.randint(i, n-1) # place to swap with (without replacement)
        mapped_item = history.get(rand_idx, rand_idx) # item store in rand-idx of the imagingary array
        current_item = history.get(i, i) # item stored in i-th index of the imaginary array
        history[i] = mapped_item
        history[rand_idx] = current_item

    return [history[i] for i in range(k)]


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('random_subset.py', 'random_subset.tsv',
                                       random_subset_wrapper))
