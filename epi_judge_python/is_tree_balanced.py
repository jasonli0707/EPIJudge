from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def brute_force(root):
    """brute force solution
    O(n^2) Time Complexity
    O(n) Space for call stack
    """
    def maxDepth(root):
        if not root:
            return 0

        return max(maxDepth(root.left), maxDepth(root.right)) + 1

    if not root:
        return True

    if abs(maxDepth(root.left) - maxDepth(root.right)) > 1:
        return False

    return brute_force(root.left) and brute_force(root.right)

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    """check if the binary tree is height balanced
       Time: O(n)
       Space: O(h) # height of tree
    """

    def dfs(root):
        if not root: return (True, 0)

        is_balanced_left, height_left = dfs(root.left)
        is_balanced_right, height_right = dfs(root.right)

        is_balanced = is_balanced_left and is_balanced_right and abs(height_left - height_right) <= 1
        height = max(height_left, height_right) + 1

        return [is_balanced, height]

    return dfs(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
