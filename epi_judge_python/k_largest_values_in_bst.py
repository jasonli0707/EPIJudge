from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils
from collections import deque


def find_k_largest_in_bst_inorder(tree, k):
    """
    Time: O(n)
    Space: O(n)
    """
    bst_queue = deque()
    def inorder(tree, k):
        if not tree:
            return 
        inorder(tree.left, k)
        bst_queue.append(tree.data)
        inorder(tree.right, k)
    inorder(tree, k)
    return [bst_queue.pop() for _ in range(k)]

def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    """
    Time: O(h+k), where h is height of the tree
    Space: O(h+k)
    """
    def reverse_inorder(tree, k):
        if tree and len(result) < k:
            reverse_inorder(tree.right, k)
            if len(result) < k:
                result.append(tree.data)
                reverse_inorder(tree.left, k)

    result = []
    reverse_inorder(tree, k)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
