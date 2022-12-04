from test_framework import generic_test
import functools


def brute_force(t ,s):
    '''
    Time: O(m*n)
    '''
    n, m = len(t), len(s)
    for i in range(n):
        if t[i:i+m] == s:
            return i
    return -1

def rabin_karp(t: str, s: str) -> int:
    '''
    Time: O(m+n)
    '''
    if len(s) > len(t):
        return -1

    def hash_code(l): # ord -> ascii table
        return functools.reduce(lambda running, x: running*26+ord(x), l, 0)

    hash_s = hash_code(s)
    hash_t = hash_code(t[:len(s)])
    power_s = 26**(len(s)-1)

    for i in range(len(s), len(t)): #O(n)
        if  hash_t == hash_s and t[i-len(s):i] == s: # O(m)
            return i - len(s)

        # rolling hash
        hash_t -= ord(t[i-len(s)])*power_s # substract leading digit
        hash_t = hash_t*26 + ord(t[i]) # add subsequence digit

    if hash_t == hash_s and t[-len(s):] == s: # when len(s) == len(t)
        return len(t) - len(s)

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
