from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L

    even_head, odd_head = ListNode(0), ListNode(0) 
    even_tail, odd_tail = even_head, odd_head

    while L and L.next:
        even_node, odd_node, temp = L, L.next, L.next.next
        even_tail.next = even_node
        odd_tail.next = odd_node
        even_node.next, odd_node.next = None, None
        even_tail = even_tail.next
        odd_tail = odd_tail.next
        L = temp

    if L: # if the length of list L is odd, appends the last element to the end of even list
        even_tail.next = L
        even_tail = even_tail.next 

    even_tail.next = odd_head.next # merge two lists

    return even_head.next

    
def even_odd_merge_sol2(L):
        if not (L and L.next):
            return L

        even, odd = L, L.next       
        odd_head = odd

        while odd and odd.next:
            even.next = odd.next
            even = even.next

            odd.next = even.next
            odd = odd.next

        
        even.next = odd_head

        return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge_sol))
