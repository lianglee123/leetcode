from typing import *

class Solution:
    """
    我自己写的深度搜索
    其中有以下几个效率低下的问题：
        1. 前缀相同的path， 每次eval时，存在重复计算
        2. 每次截断numStr, 并生成新的，有些效率低下，应该使用index
    """
    def addOperators(self, numStr: str, target: int) -> List[str]:
        res = []
        path = []
        self.helper(res, path, numStr, target)
        return res

    def helper(self, res, path, numStr, target):
        if not numStr:
            if self.eval(path) == target:
                res.append(path[:])
            return
        for i in range(1, len(numStr)+1):
            path.append(numStr[:i])
            nextNumStr = numStr[i:]
            if nextNumStr:
                for op in ("*", "+", "-"):
                    path.append(op)
                    self.helper(res, path, nextNumStr, target)
                    path.pop()
            else:
                self.helper(res, path, nextNumStr, target)
            path.pop()


    def eval(self, path: List[str]) -> int:
        return 10


class Solution2:
    def addOperators(self, numStr: str, target: int) -> List[str]:
        res = []
        self.helper(res, "", numStr, target, 0, 0)
        return res

    def helper(self, res: List, path: str, numStr: str, target: int, pos: int, eval: int):
        if pos == len(numStr):
            # if target == eval:
            res.append(path)
            return
        for i in range(pos, len(numStr)):
            # if i != pos and numStr[pos] == '0': break  防止数字开头为零的情况出现
            curNumStr = numStr[pos:i+1]
            curNum = int(curNumStr)
            if pos == 0:
                self.helper(res, path + curNumStr, numStr, target, i+1, curNum)
            else:
                self.helper(res, path + "+" + curNumStr, numStr, target, i+1, eval + curNum)
                self.helper(res, path + "-" + curNumStr, numStr, target, i+1, eval - curNum)
                self.helper(res, path + "*" + curNumStr, numStr, target, i+1, eval * curNum)




if __name__ == '__main__':
    from pprint import pprint
    s = Solution2().addOperators
    pprint(s("10005", 10))


