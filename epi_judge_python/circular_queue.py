from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.head = self.tail = 0 # empty queue
        self.arr = [None] * capacity
        self.n_elements = 0
        self.capacity = capacity

    def enqueue(self, x: int) -> None:
        # dynamic resize
        if  self.n_elements >= self.capacity:
            self.capacity *= 2 # double the size of the array
            self.arr = self.arr[self.head:] + self.arr[:self.head] + [None] * (self.capacity - self.n_elements)  # move head to zero index
            self.head, self.tail = 0, self.n_elements

        self.arr[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        self.n_elements += 1

    def dequeue(self) -> int:
        if self.size() < 1 :
            raise IndexError('empty queue')
        val = self.arr[self.head]
        self.head = (self.head + 1) % self.capacity
        self.n_elements -= 1
        return val

    def size(self) -> int:
        return self.n_elements


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
