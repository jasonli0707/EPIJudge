from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque


class QueueWithMax:
    """Implement queue data structure with a max operation

    Time Complexity:
       Enqueue: O(1)
       Dequene: O(n)
       Max:     O(1)
    """
    def __init__(self) -> None:
        self._enq = deque()
        self._deq = deque()

    def enqueue(self, x: int) -> None:
        self._enq.append(x)

        while self._deq and self._deq[-1] < x:
            self._deq.pop()

        self._deq.append(x)
            

    def dequeue(self) -> int:
        val = self._enq.popleft()
        if self._deq[0] == val:
            self._deq.popleft()
        return val

    def max(self) -> int:
        return self._deq[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
