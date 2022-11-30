import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    '''
    Time: O(n)
    Space: O(1)
    '''

    # forward pass overwriting 'b' and count number of 'a'
    write_idx = a_count = 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1
        
    # backward pass replacing 'a' with 'd' 
    curr_idx = write_idx
    write_idx += a_count - 1 # writing from behind
    final_size = write_idx + 1
    for i in reversed(range(curr_idx)):
        if s[i] == 'a':
            s[write_idx-1:write_idx+1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[i]
            write_idx -= 1

    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
