from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    new_list = None

    while current:
        next_node = current.next
        current.next = new_list
        new_list = current
        current = next_node


    return new_list


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    """reverse the order of nodes between indices "start" and "finish", inclusively.

    Args:
        L (ListNode): a singly linked list
        start (int): start index (starting from 1)
        finish (int): finish index

    Returns:
        Optional[ListNode]: a linked list with a sublist from "start" to "finish" being reversed 
    """

    dummy_head = sublist_head = ListNode(0, L) # new node pointing to list L

    for _ in range(start-1):
       sublist_head = sublist_head.next # iterate to the node before the "start" node 

    current = sublist_head.next # "start" node
    for _ in range(finish-start): # iterate through the sublist
        temp = current.next
        current.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
