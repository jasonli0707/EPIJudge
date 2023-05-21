import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.

        
def brute_force(tree: BinaryTreeNode):
    """Works for general binary tree
    Time: O(n)
    Space: O(m) (i.e. max number of nodes at any single depth stored in curr_depth_nodes)
    """
    if not tree:
        return

    curr_depth_nodes = [tree]

    while curr_depth_nodes:
        m = len(curr_depth_nodes)
        if m == 1:
            curr_depth_nodes = [child for child in (curr_depth_nodes[0].left, curr_depth_nodes[0].right) if child]
            continue

        for i in range(m-1):
            curr_depth_nodes[i].next = curr_depth_nodes[i+1]

        curr_depth_nodes = [child for node in curr_depth_nodes for child in (node.left, node.right) if child]


def construct_right_sibling(tree: BinaryTreeNode) -> None:
    """Only works for perfect binary tree
    Time: O(n)
    Space: O(1)
    """

    def level_next_traverse(node: BinaryTreeNode):

        while node and node.left:
            node.left.next = node.right
            node.right.next = node.next.left if node.next else None
            node = node.next
        return

    while tree and tree.left:
        level_next_traverse(tree)
        tree = tree.left




def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(
        original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [[n.data for n in traverse_next(level)]
            for level in traverse_left(cloned)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_right_sibling.py',
                                       'tree_right_sibling.tsv',
                                       construct_right_sibling_wrapper))
