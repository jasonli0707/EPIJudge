from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def insertion_sort_list(L):
    """
    Time: O(n^2)
    Space: O(1)
    """
    if not L:
        return L

    dummy_head = ListNode(0, L)
    pre, cur = L, L.next
    while cur:
        if pre.data <= cur.data:
            pre, cur = cur, cur.next
        else:
            tmp = dummy_head
            while cur.data > tmp.next.data: 
                tmp = tmp.next
            pre.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = pre.next
        
    return dummy_head.next


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    """
    merge sort
    Time: O(nlogn)
    Space: O(n)
    """

    if not L or not L.next: # empty or only one node
        return L

    def get_mid_node(L):
        slow, fast = L, L.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def merge_list(L1, L2):
        head = tail = ListNode(0, None)
        while L1 and L2:
            if L1.data < L2.data:
                tail.next = L1
                L1 = L1.next
            else:
                tail.next = L2
                L2 = L2.next
            tail = tail.next
           
        if L1:
            tail.next = L1 
        if L2:
            tail.next = L2

        return head.next

    # split list into halves
    left = L   
    tmp = get_mid_node(L)
    right = tmp.next
    tmp.next = None

    return merge_list(stable_sort_list(left), stable_sort_list(right))



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('insertion_sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
