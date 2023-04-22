import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def length(l):
        size = 0
        while l:
            l = l.next
            size += 1
        return size

    l0_size, l1_size = length(l0), length(l1)

    if l0_size > l1_size:
        diff = l0_size - l1_size
        short_iter = l1
        long_iter = l0
    else:
        diff = l1_size - l0_size
        short_iter = l0
        long_iter = l1

    for _ in range(diff):
        long_iter = long_iter.next

    while short_iter and long_iter and short_iter is not long_iter:
        short_iter, long_iter = short_iter.next, long_iter.next

    return short_iter


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
