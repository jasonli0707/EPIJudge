from test_framework import generic_test


MAPPING = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def roman_to_integer(s: str) -> int:
    '''
    Time: O(n)
    Space: O(1)
    '''
    sum = i = 0
    prev = 1001
    while i < len(s):
        curr = MAPPING[s[i]] 
        if  curr > prev:
            sum = sum + curr - 2*prev
        else:
            sum += curr
        prev = MAPPING[s[i]]
        i += 1

    return sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
