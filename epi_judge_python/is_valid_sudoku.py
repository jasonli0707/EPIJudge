from typing import List
from test_framework import generic_test

import math


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def has_duplicates(l):
        l = list(filter(lambda x: x!=0, l))
        return len(l) != len(set(l))

    n = len(partial_assignment)
    # check rows and cols
    if any(has_duplicates([partial_assignment[i][j] for i in range(n)]) or has_duplicates([partial_assignment[j][i] for i in range(n)])  for j in range(n)):
        return False


    # check subgrids
    m = int(math.sqrt(n))
    if any(has_duplicates([partial_assignment[k][l] for k in range(i*m, i*m+m) for l in range(j*m, j*m+m)]) # k:0,1,2, l:0,1,2 | 3,4,5 | 6,7,8 ...
           for i in range(m) for j in range(m)): # i:0, j:0,1,2 ...
        return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
