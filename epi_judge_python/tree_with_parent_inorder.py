from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    """Nonrecursive inorder traversal with O(1) Space. Nodes have parent fields.
       Time: O(n)
    """
    prev, result = None, []

    while tree:
        if prev is tree.parent: # come down to right or left child
            if tree.left: # left child
                next = tree.left
            else: # leaves
                result.append(tree.data)
                next = tree.right or tree.parent # if right child is not None, assigns tree.right to next (short circuit)
        elif tree.left is prev: # come up from left child
            result.append(tree.data)
            next = tree.right or tree.parent 
        else: # come up from right child
            next = tree.parent
            
        prev, tree = tree, next

    return result 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
