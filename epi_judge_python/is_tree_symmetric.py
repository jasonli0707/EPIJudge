from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    """Check if a binary tree is symmetric or not
       Time: O(n)
       Space: O(h)
    """
    if not tree:
        return True

    def check_symmetric(node0, node1):
        if not node0 and not node1: # both empty
            return True
        elif node0 and node1 and (node0.data == node1.data): # both not empty
           return check_symmetric(node0.left, node1.right)  and check_symmetric(node1.left, node0.right) 
        else: #  one of them is empty  
            return False

    return check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
