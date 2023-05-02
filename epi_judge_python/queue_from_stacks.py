from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    """implement a queue from stacks
       O(1) enqueue 
       O(1) dequeue if stack 2 is not empty else O(m) dequeue (number of elements in stack 1)
    """
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def enqueue(self, x: int) -> None:
        self.s1.append(x)
        return

    def dequeue(self) -> int:
        if not self.s2: # if empty
            while self.s1:
                self.s2.append(self.s1.pop())

        if not self.s2: # still empty
            raise IndexError('empty queue')
        return self.s2.pop()


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
