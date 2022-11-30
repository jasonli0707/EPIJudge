import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].


def reverse_words(s):
    '''
    Time: O(1)
    Space: O(n)
    '''
    # reverse the whole string
    s.reverse()

    def reverse_a_word(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    # reverse each word
    start = 0
    while True:
        end = -1
        for i in range(start, len(s)):
            if s[i] == ' ':
                end = i
                break
        if end < 0: # end=-1 when no white space is found
            break
        reverse_a_word(s, start, end - 1)  
        start = end + 1

    # reverse the last word
    reverse_a_word(s, start, len(s)-1)




@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    s= [' ', ' ', '9', 'Z', 'o', 'A', 'z', 'q']
    reverse_words(s)
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
