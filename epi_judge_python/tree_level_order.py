from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    """return the level order traversal of a binary tree nodes' values
       O(n) Time
       O(m) Space (i.e. max number of nodes at any single depth stored in curr_depth_nodes)
    Args:
        tree (BinaryTreeNode)

    Returns:
        List[List[int]]: list of list of nodes at each level
    """
    results = []
    if not tree:
        return results

    curr_depth_nodes = [tree]

    while curr_depth_nodes:
        results.append([node.data for node in curr_depth_nodes])
        curr_depth_nodes = [child for node in curr_depth_nodes for child in (node.left, node.right) if child]

    return results
        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
