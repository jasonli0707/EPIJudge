from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    '''
    Use arrays to simulate integer multiplication with arbitrary precision
    Time: O(nm)
    Space: O(n+m)
    '''
    sign = -1 if num1[0]*num2[0] < 0 else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0]*(len(num1)+len(num2)) # size of product of two integers at most m+n
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i+j+1] += num1[i]*num2[j] # starting from lsd: m+n-1
            result[i+j] += result[i+j+1] // 10 # carry out
            result[i+j+1] %= 10 # remainder

    # remove all leading zeros
    # next(iterator, default): get the index of first nonzero element, or else return default len(result) - 1 if all elements are zeros
    # slice result from above index to the end of array
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)-1):]
    return [sign*result[0]] + result[1:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
