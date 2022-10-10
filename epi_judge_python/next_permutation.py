from operator import inv
from typing import List

from test_framework import generic_test



def next_permutation(perm: List[int]) -> List[int]:
    '''
    Return the next permutation in the ordered permutation dictionary e.g. [2,1,0] > [2,0,1]
    Time: O(n)
    Space: O(1)
    '''
    inversion_point = len(perm)-2
    while inversion_point>=0 and (perm[inversion_point] >= perm[inversion_point+1]) :
        inversion_point -= 1

    if inversion_point == -1: # already the largest permutation
        return []

    for i in reversed(range(inversion_point+1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[i], perm[inversion_point] = perm[inversion_point], perm[i]
            break

    perm[inversion_point+1:] = perm[inversion_point+1:][::-1]

    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
