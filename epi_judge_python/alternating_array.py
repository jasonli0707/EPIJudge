import functools
from re import A
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName, TestFailure
from test_framework.test_utils import enable_executor_hook

def sort_interleave(A):
    '''
    Time: O(nlogn) (for sorting)
    Space: O(n)
    '''
    n = len(A)
    if n%2!=0: # if odd
        center = n//2+1
    else:
        center = n//2
    A.sort()
    B = A[:center] 
    C = A[center:]
    A[::2] = B
    A[1::2] = C
    return 
    

def rearrange(A: List[int]) -> None:
    '''Time O(n), Space O(1)'''
    for i in range(len(A)-1):
        if (i % 2==0) and (A[i]>A[i+1]):
            A[i], A[i+1] = A[i+1], A[i]
        elif (i%2!=0) and (A[i]<A[i+1]):
            A[i], A[i+1] = A[i+1], A[i]
    return 

    
def simplified_version(A):
    '''Complexity same as above'''
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=i%2) # if even, then reverse=False (sort in ascending); else, reverse=True (sort in descending)
    return 
    


@enable_executor_hook
def rearrange_wrapper(executor, A):
    def check_answer(A):
        for i in range(len(A)):
            if i % 2:
                if A[i] < A[i - 1]:
                    raise TestFailure().with_property(
                        PropertyName.RESULT, A).with_mismatch_info(
                            i, 'A[{}] <= A[{}]'.format(i - 1, i),
                            '{} > {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i] < A[i + 1]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] >= A[{}]'.format(i, i + 1),
                                '{} < {}'.format(A[i], A[i + 1]))
            else:
                if i > 0:
                    if A[i - 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] >= A[{}]'.format(i - 1, i),
                                '{} < {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i + 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] <= A[{}]'.format(i, i + 1),
                                '{} > {}'.format(A[i], A[i + 1]))

    executor.run(functools.partial(rearrange, A))
    check_answer(A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('alternating_array.py',
                                       'alternating_array.tsv',
                                       rearrange_wrapper))
