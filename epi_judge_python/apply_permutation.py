from typing import List

from test_framework import generic_test

def brute_force(perm, A):
    '''
    apply a given permutation to an array e.g. A = [a,b,c,d], perm = <2, 0, 1, 3> => result = [b, c, a, d]
    Time: O(n)
    Space: O(n)
    '''
    result = [None]*len(A) 
    for i in range(len(A)):
        result[perm[i]] = A[i]

    A[:] = result 


def apply_permutation(perm: List[int], A: List[int]) -> None:
    '''
    decompose permutation into independent elementwise  cyclic permutations 
    Time: O(n)
    Space: O(1)
    '''
    for i in range(len(A)):
        next = i
        while perm[next] >= 0: # destination of next element
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next] # destination of the current element
            perm[next] -= len(A) # -ve means the element has already been moved
            next = temp
    
    # restore perm array
    perm[:] = [e+len(A) for e in perm]



def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
