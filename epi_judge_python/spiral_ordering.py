from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    """
    Time Complexity: O(n^2)
    """
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    d = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix)**2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0

        next_x, next_y = x + directions[d][0], y + directions[d][1]
        if (next_x not in range(len(square_matrix)) or next_y not in range(len(square_matrix)) or square_matrix[next_x][next_y]==0):
            # skip out of range indices or elements which have been visited
            d = (d+1) & 3 # select first two bits i.e. 5 & 3 = 101 & 011 -> 01 = 1
            next_x, next_y = x + directions[d][0], y+directions[d][1]

        x, y = next_x, next_y

    return spiral_ordering


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
