from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    """delete the kth last node in L

    Args:
        L (ListNode): a singly linked list
        k (int): index of kth last node 

    Returns:
        Optional[ListNode]: linked list with k-th node deleted 
    """
    first = L
    second = dummy_head = ListNode(0, L) # (k+1)-th node to delete k-th node

    for _ in range(k):
        first = first.next

    while first:
        first, second = first.next, second.next

    second.next = second.next.next

    return dummy_head.next # dummy head is necessary as the first node can be the k-th last node


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
