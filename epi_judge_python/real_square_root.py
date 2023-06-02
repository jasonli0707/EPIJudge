from test_framework import generic_test
import math


def square_root(x: float) -> float:
    l, u = (1.0, x) if x > 1.0 else (x, 1.0)

    while not math.isclose(l, u):
        m = l + (u-l)/2
        m2 = m*m 
        diff = m2 - x
        
        if diff > 0: # m2 > x
            u = m
        else: # m2 <= x
            l = m

    return l


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
