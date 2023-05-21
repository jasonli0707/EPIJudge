import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Time: O(n)

# 1) using nonlocal to keep track of global idx
def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    idx = 0
    def recursion_helper():
        nonlocal idx  # Declare idx as nonlocal
        node = preorder[idx]
        idx += 1

        if node is None:
            return None

        left_subtree = recursion_helper()
        right_subtree = recursion_helper()
       
        return BinaryTreeNode(data=node,
                                left=left_subtree,
                                right=right_subtree
                                ) 

    return recursion_helper()

# 2) use two local variables next_idx and final_idx
def reconstruct_preorder2(preorder: List[int]) -> BinaryTreeNode:
    def recursion_helper(idx):
        node = preorder[idx]
        idx += 1

        if node is None:
            return None, idx

        left_subtree, next_idx = recursion_helper(idx)
        right_subtree, final_idx = recursion_helper(next_idx)

        return BinaryTreeNode(data=node,
                              left=left_subtree,
                              right=right_subtree
                             ), final_idx

    tree, _ = recursion_helper(0)
    return tree

# 3) use an iterator with builtin attribute
def reconstruct_preorder3(preorder: List[int]) -> BinaryTreeNode:
    def recursion_helper(iter):
        node = next(iter)

        if node is None:
            return None

        left_subtree = recursion_helper(iter)
        right_subtree = recursion_helper(iter)

        return BinaryTreeNode(data=node,
                              left=left_subtree,
                              right=right_subtree
                             )

    return recursion_helper(iter(preorder))


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
