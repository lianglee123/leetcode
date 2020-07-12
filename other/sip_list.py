import random


class SkipNode:
    def __init__(self, key: float, val: object, next=None):
        self.key = None
        self.val = None
        self.next = next if next else []

    def getLevelNode(self, level):
        if level < len(self.next):
            return self.next[level]
        else:
            return None




class SkipList:

    LEVEL_LIMIT = 32
    P = 0.25

    def __init__(self):
        self.header = SkipNode(0, None, next=[SkipNode(0, 0)])

        self.maxLevel = 0
        self.nodeCount = 0



    def Find(self, key) -> SkipNode:
        x = self.header
        for level in reversed(range(self.maxLevel)):
            while x.getLevel(level) and x.getLevel(level).key < key:
                x = x.getLevel(level)
        x = x.next[0]
        if x and x.key == key:
            return x

    def Delete(self, key) -> bool:
        updateNodes = [None] * self.LEVEL_LIMIT

        # level向下降，x向右走, 记录走过的所有Node, 当建立新Node时，这些Node的层级有可能会被影响
        x = self.header
        for level in reversed(range(self.maxLevel)):
            while x.next[level] and x.next[level].key < key:
                x = x.getLevel(level)
            updateNodes[level] = x
        x = x.next[0]
        if not x:
            return False
        if x.key == key:
            for level in range(self.maxLevel):
                if updateNodes[level].next[level] != x:
                    break
                else:
                    updateNodes[level] = x.next[level]
            self.nodeCount -= 1
            while self.maxLevel >= 1 and len(self.header.next) > self.maxLevel and not self.header.next[self.maxLevel-1]:
                self.maxLevel -= 1

    def Insert(self, key, val) -> SkipNode:
        updateNodes = [None] * self.LEVEL_LIMIT

        # level向下降，x向右走, 记录走过的所有Node, 当建立新Node时，这些Node的层级有可能会被影响
        x = self.header
        for level in reversed(range(self.maxLevel)):
            while x.getLevel(level) and x.getLevel(level).key < key:
                x = x.getLevel(level)
            updateNodes[level] = x

        x = x.next[0]
        if x and x.key == key:
            x.val = val
            return x
        newLevel = self.randomLevel()
        if newLevel > self.maxLevel:
            for level in range(self.maxLevel+1, newLevel):
                updateNodes[level] = self.header
            self.maxLevel = newLevel

        newNode = SkipNode(key, val, next=[None]*newLevel)
        for level in range(newLevel):
            newNode.next[level] = updateNodes[level].next[level]
            updateNodes[level].next[level] = newNode

        return newNode






    def __len__(self):
        return self.nodeCount


    def randomLevel(self):
        level = 1
        while random.random() < self.P:
            level += 1
            if level >= self.LEVEL_LIMIT:
                return self.LEVEL_LIMIT
        return level
