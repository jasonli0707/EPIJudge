from test_framework import generic_test
import itertools



def look_and_say_pythonic(n):
    # groupby() groups consecutive sequence
    s = '1'
    for _ in range(n-1):
        s = ''.join([str(len(list(group))) + key for key, group in itertools.groupby(s)])
    return s

def look_and_say(n: int) -> str:
    '''
    Time: O(n*2^n) upper bound
    Explanation: 
    next number is at most twice as many digits as prev one when all digits are distinct => max length is smaller or equal to 2^n
    each iteration is proportion to the number of digits n in the string s 
    '''
    s = '1'
    for _ in range(n-1):
        i = 0
        result = []
        while i < len(s): # one particular group
            count = 1
            while i + 1 < len(s) and s[i] == s[i+1]: # consecutive equal digit
                count += 1
                i += 1
            result.append(str(count) + s[i])
            i += 1
        s = ''.join(result)
    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
