class Integer:
    def __init__(self, v):
        self.v = v


class Solution:
    """
    https://www.cnblogs.com/grandyang/p/5203228.html
    """
    def strobogrammaticInRange(self, low, high):
        res = Integer(0)
        self.find(low, high, '', res)
        self.find(low, high, '0', res)
        self.find(low, high, '1', res)
        self.find(low, high, '8', res)
        return res.v

    def find(self, low, high, path, res):
        if len(path) + 2 > len(high):
            return
        if len(low) <= len(path) <= len(high):
            if len(path) == len(high) and path > high:  # 数字字符串的大小比较，必须基于长度相同的情况
                return
            if len(path) == len(low) and path < low:
                return
            if not (len(path) > 1 and path[0] == '0'):
                res.val += 1
        self.find(low, high, "0" + path + '0', res)
        self.find(low, high, "1" + path + '1', res)
        self.find(low, high, "8" + path + '8', res)
        self.find(low, high, "6" + path + '9', res)
        self.find(low, high, "9" + path + '6', res)
