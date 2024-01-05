from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import deque, namedtuple


# recursive DFS (preorder)
def is_binary_tree_bst(tree: BinaryTreeNode, low_bound=float('-inf'), high_bound=float('inf')) -> bool:
    '''
    Time: O(n), visit the left subtree first
    Space: O(h), where h is the height of the tree
    '''
    if not tree: 
        return True
    elif not (low_bound<=tree.data<=high_bound):
        return False
    return is_binary_tree_bst(tree.left, low_bound=low_bound, high_bound=tree.data)  and is_binary_tree_bst(tree.right, low_bound=tree.data, high_bound=high_bound)

# iterative BFS with queue
def is_binary_tree_bst_iter(tree):
    '''
    Time: O(n), faster when the violating node is located near the root (shallow)
    Space: O(n), worst case: complete binary tree where the queue at most stores n/2 elements
    '''
    QueueEntry = namedtuple('QueueEntry', ['node','low_bound','high_bound']) 
    bfs_queue = deque([QueueEntry(tree, low_bound=float('-inf'), high_bound=float('inf'))])
    while bfs_queue:
        curr_entry = bfs_queue.popleft()
        if curr_entry.node:
            if not curr_entry.low_bound<=curr_entry.node.data<=curr_entry.high_bound:
                return False
            bfs_queue.extend([QueueEntry(curr_entry.node.left, low_bound=curr_entry.low_bound, high_bound=curr_entry.node.data), 
                              QueueEntry(curr_entry.node.right, low_bound=curr_entry.node.data, high_bound=curr_entry.high_bound)])
    return True
    

# recursive DFS (inorder traversal)
def is_binary_tree_bst_inorder(tree):
    '''
    Time: O(n)
    Space: O(h)
    Inorder traversal of BST will give us a sorted list
    '''
    prev = float("-inf")
    def inorder(tree):
        nonlocal prev
        if not tree:
            return True
        if not (inorder(tree.left) and prev <= tree.data):
            return False
        prev = tree.data
        return inorder(tree.right)
    return inorder(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst_inorder))
