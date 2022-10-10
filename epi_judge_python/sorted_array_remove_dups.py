import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def brute_force(A) -> int:
    '''
    Use a hash table to keep track of new elements
    Time: O(n)
    Space: O(n)
    '''
    new = {} 
    B = []
    for i, e in enumerate(A):
        if e not in new:
            new[e] = 1
            B.append(e)
    A[:] = B # deep copy
    return len(new)

# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    """remove duplicates in sorted array inplace and return the number of valid elements
       Time: O(n)
       Space: O(1)
    Args:
        A (List[int]): a sorted array

    Returns:
        int: the number of valid elements
    """
    if not A: # empty list
        return 0

    i = 0
    j = 1
    while j< len(A):
        if A[i] == A[j]:
            j+=1
        else:
            A[i+1] = A[j]
            i+=1
            j+=1
    A = A[:i+1]
    return len(A)



@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
