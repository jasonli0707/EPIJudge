from test_framework import generic_test
import string


def shortest_equivalent_path(path: str) -> str:
    if not path:
        raise ValueError("Invalid Path")

    path_names = []

    # special case when path starts with /
    if path[0] == '/':
        path_names.append('/')


    for token in (token for token in path.split('/') if token not in ['.', '']): # ignore . or empty token
        if token == '..':
            if not path_names or path_names[-1] == '..': # if last path name is .. or empty stack
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError("Path Error")
                path_names.pop()
        else:
            path_names.append(token)
    result = '/'.join(path_names)
    return result[result.startswith('//'):] # if result start with // => start from index 1 i.e. skip one /


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))