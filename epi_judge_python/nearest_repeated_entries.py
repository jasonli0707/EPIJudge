from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    vocab = {}
    min_dist = len(paragraph) + 1
    for i, w in enumerate(paragraph):
        if w not in vocab:
            vocab[w] = i
        else:
            dist = i - vocab[w]
            vocab[w] = i
            min_dist = min(dist, min_dist)

    return min_dist if min_dist < len(paragraph) else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
