import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def hash_solution(head):
    # O(n) time and O(n) space solution with hash table
    visited = set()

    current = head
    while current:
        if id(current) in visited:
            return current
        else:
            visited.add(id(current))
        current = current.next

    return None


def brute_force(head):
    # O(n^2) time and O(1) space solution
    outer = head
    i = 0
    while outer:
        outer = outer.next
        i += 1
        inner = head
        for _ in range(i):
            if id(inner) == id(outer):
                return outer
            inner = inner.next
    return None

def has_cycle(head: ListNode) -> Optional[ListNode]:
    """Floyd's Cycle-Finding algorithm  or Hare-Tortoise algorithm
        It is also called Hare-Tortoise algorithm
        The algorithm works by using two pointers, a slow pointer and a fast pointer.
        Initially, both pointers are set to the head of the linked list.
        The fast pointer moves twice as fast as the slow pointer.
        If there is a cycle in the linked list, eventually, the fast pointer will catch up with the slow pointer.
        If there is no cycle, the fast pointer will reach the end of the linked list.

       O(n) Time and O(1) Space
    Args:
        head (ListNode): A singly linked list

    Returns:
        Optional[ListNode]: return None if no cycle is found else return the node where the cycle begins.
    """
    fast = slow = head
    while fast and fast.next and fast.next.next: # need at least two nodes to form a cycle
        slow, fast = slow.next, fast.next.next # fast advances twice as fast
        if slow is fast: # cycle exits when two meets
            slow = head # reset
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow

    return None


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
