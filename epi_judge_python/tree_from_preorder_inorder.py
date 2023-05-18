from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:

    """
    Time: O(n) i.e. O(1) per node
    Space: O(n+h) i.e. O(n) hash table, O(h) call stack
    """

    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)} # O(n) hash table

    def recursion_helper(in_start, in_end, pre_start, pre_end):
        
        # base case
        if in_start >= in_end or pre_start >= pre_end:
            return None

        root = preorder[pre_start] # the first element of preorder traversal is the root
        root_idx = node_to_inorder_idx[root]
        left_tree_size = root_idx - in_start # size of left subtree is determined by the inorder traversal

        return BinaryTreeNode   (
           data=root,
           left=recursion_helper(in_start, root_idx, pre_start+1, pre_start+1+left_tree_size), # inorder[in_start:root_idx], preorder[pre_start+1:pre_start+1+left_tree_size]
           right=recursion_helper(root_idx+1, in_end, pre_start+1+left_tree_size, pre_end) # inorder[root_idx+1, in_end], preorder[pre_start+1+left_tree_size:pre_end]
        )

    return recursion_helper(0, len(inorder), 0, len(preorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
