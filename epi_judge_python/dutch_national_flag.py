import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

def brute_force(pivot_index, A):
    ''' O(n^2) time, O(1) space'''
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i] # move small elements to the start
                break # move i to i + 1

    for i in reversed(range((len(A)))):
        if A[i] < pivot: # advancing from the back, if A[i] reaches element < pivot -> ends sorting
            break
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i] # move large elements to the end
                break # move i to i+1
    return 


def one_pass(pivot_index, A):
    '''O(n) time and O(1) space'''
    pivot = A[pivot_index]
    smaller = 0 # keep track of last element larger than pivot
    for i in range(len(A)):
        if A[i] < pivot:
            A[smaller], A[i] = A[i], A[smaller]
            smaller += 1
    # at this point all elements smaller than A is moved to the front
    
    larger = len(A) - 1 # keep track of last element smaller than pivot
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        if A[i] > pivot:
            A[larger], A[i] = A[i], A[larger]
            larger -= 1
    return 

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    """
    Reorder the elements of an array with all elements less than pivot appear first, followed by those equal to pivot, followed by elements greater than pivot
    reference: https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
    smaller: A[:low]
    equal: A{low:mid}
    unclassified: A[mid:high]
    larger: A[high:]
    A = [<|=|?|>]
    O(n) time and O(1) space
    """
    pivot = A[pivot_index]
    low, mid, high = 0, 0, len(A) - 1
    while mid <= high:
        if A[mid] < pivot:
            A[low], A[mid] = A[mid], A[low]
            low+=1
            mid+=1
        elif A[mid] == pivot:
            mid+=1
        else: # A[mid] > pivot
            A[high], A[mid] = A[mid], A[high]
            high-=1
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
