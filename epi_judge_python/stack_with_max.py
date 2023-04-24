from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import namedtuple


class StackCachedMax:
    """Stack implementation with max operation using caching

       O(1) time for all operations
       O(n) additional space for caching max elements
    """
    ElementWithCachedMax = namedtuple('ElementWithCachedMax', ['element', 'max']) # similar to struct in C++

    def __init__(self):
        self._elements_with_cached_max = [] # array of namedtuple

    def empty(self) -> bool:
        return len(self._elements_with_cached_max) == 0

    def max(self) -> int:
        if self.empty():
            raise IndexError("max(): empty stack")
        return self._elements_with_cached_max[-1].max

    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop(): empty stack")
        return self._elements_with_cached_max.pop().element

    def push(self, x: int) -> None:
        self._elements_with_cached_max.append(self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max())))

        
class StackMaxCount:
    """Stack implementation with max operation by keep track of max counts

       O(1) time for all operations
       O(1) best-case and O(n) worst-case additional space for keeping track of max elements
    """
    class MaxWithCount: # keep track of the counts of max elements
        def __init__(self, max, count):
            self.max = max
            self.count = count

    def __init__(self):
        self._s = []
        self._max_count_s = []

    def empty(self) -> bool:
        return len(self._s) == 0

    def max(self) -> int:
        if self.empty():
            raise IndexError("max(): empty stack")
        return self._max_count_s[-1].max

    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop(): empty stack")

        x = self._s.pop()  
        current_max = self._max_count_s[-1].max # cannot call self.max() as self._s may already be empty after pop
        if x == current_max:
            self._max_count_s[-1].count -= 1
            if self._max_count_s[-1].count == 0:
                self._max_count_s.pop()
        return x

    def push(self, x: int) -> None:
        self._s.append(x)
        if len(self._max_count_s) == 0: # cannot call self.empty() as we already push x into self._s 
            self._max_count_s.append(self.MaxWithCount(x, 1))
        else:
            current_max = self.max()
            if x == current_max:
                self._max_count_s[-1].count += 1
            elif x>current_max:
                self._max_count_s.append(self.MaxWithCount(x, 1))



def stack_tester(ops):
    try:
        s = StackMaxCount()

        for (op, arg) in ops:
            if op == 'Stack':
                s = StackMaxCount()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
