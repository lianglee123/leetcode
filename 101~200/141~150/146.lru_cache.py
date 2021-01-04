

class DLinkList:
    def __init__(self, key, val, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

    def __repr__(self):
        return "Node[key=%s, val=%s]" % (self.key, self.val)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curSize = 0
        self.cache = {}
        self.usedRecord = []
        self.headGuard = DLinkList(None, None)
        self.tailGuard = DLinkList(None, None)
        self.headGuard.next = self.tailGuard
        self.tailGuard.pre = self.headGuard

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        if key not in self.cache:
            return -1
        node = self.cache.get(key)
        self.__moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            self.__moveToHead(node)
            node.val = value
        else:
            if self.curSize >= self.capacity:
                self.__popFromTail()
            node = DLinkList(key, value)
            self.cache[key] = node
            self.__addNewToHead(node)
            self.curSize += 1

    def __moveToHead(self, node):
        node.next.pre = node.pre
        node.pre.next = node.next
        self.__addNewToHead(node)

    def __addNewToHead(self, node):
        node.next = self.headGuard.next
        node.pre = self.headGuard
        self.headGuard.next.pre = node
        self.headGuard.next = node


    def __popFromTail(self):
        popNode = self.tailGuard.pre
        popNode.pre.next = self.tailGuard
        self.tailGuard.pre = popNode.pre
        popNode.pre, popNode.next = None, None
        self.cache.pop(popNode.key)


if __name__ == '__main__':
    lru = LRUCache(3)
    lru.put(1, 1)
    print(lru.cache)
    lru.put(2, 2)
    lru.put(3, 3)
    lru.put(4, 4)
    print(lru.cache)
    assert lru.get(1) == -1
    assert lru.get(4) == 4
    assert lru.get(3) == 3
    assert lru.get(2) == 2
    lru.put(5, 4)
    assert lru.get(4) == -1

