import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    return random.randrange(2)


def uniform_random(lower_bound: int, upper_bound: int) -> int:
    """generate a random integer between lower_bound and upper_bound, inclusive, with equal probability
    , given a binary random number generator

    Time Complexity: O(n) or O(log(a+b-1)) i.e. 2^n - 1 = b - a
    """
    diff = upper_bound - lower_bound

    while True: # run until the generated result is within the range [0, diff]
        n_bits, result = 0, 0

        while (1<<n_bits) - 1 <= diff: # The max number represented by n-bits: 2^(n) - 1 needs to be smaller than diff
            result = (result<<1) | zero_one_random()
            n_bits += 1

        if result <= diff: # if the generated result is within the range, then breaks the while loop
            break

    return result + lower_bound 


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda:
            [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('uniform_random_number.py',
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
