from typing import *


class Solution:
    """
    DFS:
    从所有零的位置开始搜索
     - 从为零的位置开始向四面八方扩展
        - 如果为-1(碰到墙壁)， 则保持不变，停止dfs
        - 否则：其值为min(pre+1, cur), 然后继续向下dfs
        - 当碰到边界时停止dfs
    这道题使用使用-1表示墙，INF表示room, 0表示gate, 其实是为了降低解题难度。
    如果他不是这样的表示方法，我们也应该自己转化为这样的
    """
    def wallsAndGates(self, rooms):
        if not rooms or not rooms[0]:
            return
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    self.dfs(0, i, j, rooms)

    def dfs(self, pre, i, j, rooms):
        if not self.validPos(i, j, rooms):
            return
        for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nextI = i + direction[0]
            nextJ = j + direction[1]
            if self.validPos(nextI, nextJ, rooms) and rooms[i][j] != -1:
                if pre + 1 < rooms[nextI][nextJ]:
                    rooms[nextI][nextJ] = pre + 1
                    self.dfs(pre+1, nextI, nextJ, rooms)

    def validPos(self, i, j, rooms):
        return 0 <= i < len(rooms) and 0 <= j < len(rooms[0])




class Solution2:
    """
    DFS, 别人写的,真优雅
https://www.cnblogs.com/grandyang/p/5285868.html
    """
    def wallsAndGates(self, rooms):
        if not rooms or not rooms[0]:
            return
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    self.dfs(0, i, j, rooms)

    def dfs(self, val, i, j, rooms):
        if not self.validPos(i, j, rooms) or rooms[i][j] < val:
            return
        rooms[i][j] = val
        self.dfs(val+1, i+1, j, rooms)
        self.dfs(val+1, i-1, j, rooms)
        self.dfs(val+1, i, j+1, rooms)
        self.dfs(val+1, i, j-1, rooms)


    def validPos(self, i, j, rooms):
        return 0 <= i < len(rooms) and 0 <= j < len(rooms[0])

from collections import deque

class Solution3:
    def wallsAndGates(self, rooms):
        if not rooms or not rooms[0]:
            return
        q = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    q.append((i, j))
        while q:
            i, j = q.pop()
            for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nextI = i + direction[0]
                nextJ = j + direction[1]
                if not self.validPos(nextI, nextJ, rooms):
                    continue
                curVal = rooms[i][j]
                if curVal+1 < rooms[nextI][nextJ]:
                    rooms[nextI][nextJ] = curVal + 1
                    q.appendleft((nextI, nextJ))

    def validPos(self, i, j, rooms):
        return 0 <= i < len(rooms) and 0 <= j < len(rooms[0])


if __name__ == '__main__':
    from pprint import pprint

    s = Solution().wallsAndGates

    inf = float('+inf')
    matris = [
        [inf, -1, 0, inf],
        [inf, inf, inf, -1],
        [inf, -1, inf, -1],
        [0, -1, inf, inf],
    ]
    s(matris)
    print(matris)