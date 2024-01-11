from test_framework import generic_test


def fibonacci_bottomup_iter(n):
    """
    Time: O(n)
    Space: O(1)
    """
    if n <= 1:
        return n
    f_minus_1, f_minus_2 = 1, 0
    for _ in range(n-1):
        f_n = f_minus_1 + f_minus_2
        f_minus_1, f_minus_2 = f_n, f_minus_1
    return f_n

def fibonacci(n: int, cache={}) -> int:
    """
    Time: O(n)
    Space: O(n)
    """ 
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci_bottomup_iter))
