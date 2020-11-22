from typing import *



class SimpleIterator:
    def __init__(self, values):
        self.values = values
        self.l = len(values)
        self.ptr = 0

    def hasNext(self):
        return self.ptr < self.l

    def next(self):
        res = self.values[self.ptr]
        self.ptr += 1
        return res

    def __nonzero__(self):
        return self.hasNext()


from collections import deque


class ZigzagIterator:
    def __init__(self, v1, v2):
        q = deque()
        q.push(SimpleIterator(v1))
        q.push(SimpleIterator(v2))
        self.q = q

    def next(self):
        if self.hasNext():
            return self.q[-1].next()
        raise StopIteration()

    def hasNext(self):
        while True:
            if not self.q:
                return False
            elif self.q[-1]:
                return True
            else:
                self.q.pop()


