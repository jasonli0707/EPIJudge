from test_framework import generic_test


def square_root(k: int) -> int:
    l, r = 0, k
    while l <= r:
        m = l + (r-l) //2
        m2 = m*m
        if m2 == k:
            return m
        elif m2 > k:
            r = m - 1
        else:
            l = m + 1
    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
