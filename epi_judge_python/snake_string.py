from test_framework import generic_test


def snake_string(s: str) -> str:
    '''
    Time: O(n)
    Space: O(n)
    '''
    return s[1::4] + s[::2] + s[3::4]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
