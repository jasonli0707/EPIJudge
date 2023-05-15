import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    """find the lowest common ancestor of two nodes with parent field
       Time: O(h)
       Space: O(1)
    """
    def get_depth(node):
        depth = 0
        while node:
            node = node.parent
            depth += 1
        return depth

    depth0, depth1 = get_depth(node0), get_depth(node1)

    shallow, deep = (node0, node1) if depth0 < depth1 else (node1, node0)

    depth_diff = abs(depth0 - depth1)

    for _ in range(depth_diff): 
        deep = deep.parent

    while shallow != deep:
        shallow = shallow.parent
        deep = deep.parent

    return shallow


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
