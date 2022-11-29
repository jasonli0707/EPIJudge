from test_framework import generic_test
import functools
import string

def ss_decode_col_id(col: str) -> int:
    '''
    Time: O(n)
    Similar to question 6.1 i.e. base26 string & int conversion but starting with A=1
    '''
    
    return functools.reduce(lambda running_sum, c: running_sum*26 + (string.ascii_uppercase.index(c.upper())+1), col, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
