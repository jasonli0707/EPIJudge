from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k_inorder(tree, k):
    """
    Time: O(n)
    Space: O(h)
    """
    if not tree:
        return None

    left = find_first_greater_than_k_inorder(tree.left, k)
    if left:
        return left

    if tree.data > k:
        return tree

    return find_first_greater_than_k_inorder(tree.right,k)

def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    """
    Time: O(h)
    Space: O(1)
    """
    subtree, candidate = tree, None
    while subtree:
        if subtree.data <= k:
            subtree = subtree.right
        else:
            candidate = subtree
            subtree = subtree.left
        
    return candidate


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
