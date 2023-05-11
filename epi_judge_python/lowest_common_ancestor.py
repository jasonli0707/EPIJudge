import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    """compute the LCA of two nodes in a binary tree 
       Time: O(n)
       Space: O(h)
    """

    if not tree:
        return
    
    if tree.data == node0.data or tree.data == node1.data:
        return tree
    
    left = lca(tree.left, node0, node1)
    right = lca(tree.right, node0, node1)

    if left and right:
        return tree # if both left and right are nodes => common ancestor 
    else:
        return left or right # either one of them returns a node or both return null


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
