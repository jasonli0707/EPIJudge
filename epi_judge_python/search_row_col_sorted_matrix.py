from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    """
    Time: O(n+m) i.e. at most n+m-1 steps (eliminates one row or column each step) when x is not present in A
    """
   
    n, m = len(A), len(A[0]) # nxm matrix A
    r, c = 0, m - 1

    while c>=0 and r<n:
        if A[r][c] == x:
            return True
        elif A[r][c] > x: 
            c -= 1
        else:
            r += 1

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
