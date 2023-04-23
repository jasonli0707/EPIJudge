from list_node import ListNode
from test_framework import generic_test

def reverse_linked_list(L):
    new_list = None
    current = L
    while current:
        temp = current.next
        current.next = new_list
        new_list = current
        current = temp

    return new_list


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    """check if a singly linked list is a palindrome
       O(n) Time & O(1) Space
       - use fast and slow pointers to find the second half of the list
       - reverse it using a one-time O(n) cost
       - check if the first half equals the reversed second half

    Args:
        L (ListNode): head of the linked list

    Returns:
        bool: return True if it is a palindrome else False
    """

    fast  = slow = L
    while fast and fast.next: # if the number of nodes is odd, fast reaches the last node; else fast reaches the null
        slow, fast = slow.next, fast.next.next # fast travels twice as fast

    first_iter, second_iter = L, reverse_linked_list(slow) # second half is either of the same length or with one more nodes than first half
    while first_iter and second_iter:
        if first_iter.data != second_iter.data:
            return False
        first_iter, second_iter = first_iter.next, second_iter.next
    
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
