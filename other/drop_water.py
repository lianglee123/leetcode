class Cup:
    def __init__(self, name, cap, l=0):
        self.name = name
        self.cap = cap
        self.len = l

    def __str__(self):
        return "%s(%s)" %(self.name, self.len)



class Solution:
    """
    使用3L和5L的杯子， 如何获取4L的水？
    """

    def solve(self, target):
        self.seen = set()
        self.actions = []
        self.target = target
        c1, c2 = Cup('c5', 5), Cup('c3', 3)
        if self.dfs(c1, c2):
            return self.actions
        else:
            raise Exception("method not found")

    def dfs(self, c1, c2):
        if c1.len == self.target or c2.len == self.target:
            return True

        if (c1.len, c2.len) in self.seen:
            return False
        self.seen.add((c1.len, c2.len))

        for cmd in [Solution.dropALl, Solution.addFull, Solution.addFromCup]:
            if self.dfs(*cmd(c1, c2, self.actions)):
                return True
            self.actions.pop()

            if self.dfs(*cmd(c2, c1, self.actions)):
                return True
            self.actions.pop()

        return False

    @staticmethod
    def dropALl(c1, c2, actions):
        _c1, _c2 = Cup(c1.name, c1.cap, 0), c2
        msg = "dropAll: %s--> %s" % (c1, _c1)
        actions.append(msg)
        return _c1, _c2

    @staticmethod
    def addFull(c1, c2, actions):
        _c1, _c2 = Cup(c1.name, c1.cap, c1.cap), c2
        msg = "addFull: %s --> %s" % (c1, _c1)
        actions.append(msg)
        return _c1, _c2

    @staticmethod
    def addFromCup(c1, c2, actions):
        if c1.len + c2.len >= c1.cap:
            remainder = c1.cap - c1.len
            _c1, _c2 = Cup(c1.name, c1.cap, c1.cap), Cup(c2.name, c2.cap, c2.len - remainder)
        else:
            _c1, _c2 = Cup(c1.name, c1.cap, c1.len + c2.len), Cup(c2.name, c2.cap, 0)
        msg = "addFromCup： %s, %s--> %s, %s" % (c1, c2, _c1, _c2)
        actions.append(msg)
        return _c1, _c2


def main():
    s = Solution()
    for i, action in  enumerate(s.solve(4)):
        print(action)


if __name__ == '__main__':
    main()
