from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    """merge two sorted linked lists
       Time: worst-case: O(n+m)
       Space: O(1)

    Returns:
        Optional[ListNode]: the head of the merged linked list
    """
    dummy_head = tail = ListNode() # referencing to the same address

    while L1 and L2: # break when either one or both are empty
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next

        tail = tail.next # move tail pointer to the next node in the merged list

    tail.next = L1 or L2 # appends the remaining nodes of L1 or L2
    
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
