from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    """
    Time & Space: O(n!)
    """
    def solve_permute():
        if len(permute) == len(A):
            res.append(permute[:])
            return

        for i in range(len(A)):
            if not used[i]:
                permute.append(A[i])
                used[i] = True
                solve_permute()
                used[i] = False
                permute.pop()

    res, permute = [], []
    used = [False] * len(A)
    solve_permute()
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
