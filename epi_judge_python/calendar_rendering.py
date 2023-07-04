import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

# Event is a tuple (time, is_start)
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    """
    Time: O(nlogn)
    Space: O(n)
    """

    E = [Endpoint(event.start, True) for event in A] + [Endpoint(event.finish, False) for event in A] 
    E.sort(key=lambda e: (e.time, not e.is_start)) # sort by time, break ties with binary flag is_start i.e. starting point comes first 

    max_simultaneous_events = simultaneous_events = 0

    for e in E:
        if e.is_start:
            simultaneous_events += 1
            max_simultaneous_events = max(max_simultaneous_events, simultaneous_events)
        else:
            simultaneous_events -= 1

    return max_simultaneous_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
