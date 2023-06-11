from typing import List

from test_framework import generic_test, test_utils
from collections import defaultdict, Counter


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    """
    Time: O(nm)
    Space: O(n)
    """

    anagram_groups = defaultdict(list)

    for s in dictionary:
        freq_arr = [0]*26 # 26 characters
        for c in s: # O(m)
            if c != " ":
                freq_arr[ord(c)-97] += 1 
        key = tuple(freq_arr) # O(1) cast list to hashable tuple
        anagram_groups[key].append(s)

    return [group for group in anagram_groups.values() if len(group) > 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
