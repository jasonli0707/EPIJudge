import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    """
    Time: O(nlogn
    """
    intervals.sort(key=lambda e: (e.left.val, not e.left.is_closed))
    result = []
    i = 1
    currInterval = intervals[0]
    while i < len(intervals):
        if intervals[i].left.val < currInterval.right.val:
            if intervals[i].left.val < currInterval.left.val:
                left = intervals[i].left
            else:
                left = currInterval.left

            if intervals[i].right.val > currInterval.right.val:
                right = intervals[i].right
            elif intervals[i].right.val == currInterval.right.val and intervals[i].right.is_closed:
                right = intervals[i].right
            else:
                right = currInterval.right

            currInterval = Interval(left, right)
        elif intervals[i].left.val == currInterval.right.val and (intervals[i].left.is_closed or currInterval.right.is_closed):
            left = currInterval.left
            right = intervals[i].right
            currInterval = Interval(left, right)
        else:
            result.append(currInterval)
            currInterval = intervals[i]

        i += 1

    result.append(currInterval)

    return result


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
