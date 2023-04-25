from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    stack = []
    lookup = {'(': ')', '[': ']', '{': '}'}

    for c in s:
        if c in lookup: # open parenthesis
            stack.append(c)
        elif not stack or lookup[stack.pop()] != c: # if close parethesis => check if stack is empty or there is a mismatch
            return False

    return not stack # return True if the stack is empty


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
