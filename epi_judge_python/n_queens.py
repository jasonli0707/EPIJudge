from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    """
    return all possible distinct nonattacking placments of n queens on a nxn board
    result in form of e.g. (1, 3, 0, 2), where i-th index indicates i-th row and the value represents the column position
    """
    cols = set()
    pos_diags = set() # from lower left to upper right: r+c is constant
    neg_diags = set() # from upper left to lower right: r-c is constant

    res = []
    sol = [0]*n

    def solve_n_queens(r):
        if r == n:
            res.append(list(sol))
            return 

        for c in range(n):
            if not any([c in cols, r+c in pos_diags, r-c in neg_diags]):
                sol[r] = c
                cols.add(c)
                pos_diags.add(r+c)
                neg_diags.add(r-c)

                solve_n_queens(r+1)

                sol[r] = 0
                cols.remove(c)
                pos_diags.remove(r+c)
                neg_diags.remove(r-c)

    solve_n_queens(0)

    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
