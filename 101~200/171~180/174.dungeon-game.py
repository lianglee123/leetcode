from typing import *


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon and not dungeon[0]:
            return 0
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for i in range(m)]
        dp[-1][-1] = max(0, -dungeon[-1][-1])
        for i in range(-2, -(m+1), -1):
            pass



if __name__ == '__main__':
    s = Solution().calculateMinimumHP

