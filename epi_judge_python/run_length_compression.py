from test_framework import generic_test
from test_framework.test_failure import TestFailure
import itertools
import string


def decoding(s: str) -> str:
    result = []
    count = 0
    for c in s:
        if c.isdigit():
            count = count*10 + int(c)
        else:
            result.append(c*count)
            count = 0
    return ''.join(result)

def encoding(s: str) -> str:
    i, count = 0, 1
    result = []
    while i+1 < len(s):
        if s[i] == s[i+1]:
            count += 1
        else:
            result.append(str(count) + s[i])
            count = 1
        i+=1
    result.append(str(count) + s[i])
    return ''.join(result)

def encoding_pythonic(s: str) -> str:
    return ''.join([str(len(list(g))) + k for k, g in itertools.groupby(s)])


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
