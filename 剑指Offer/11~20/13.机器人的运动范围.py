from typing import *
from collections import deque

def __digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans


def digitsum(n1, n2):
    return __digitsum(n1) + __digitsum(n2)


# https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/ji-qi-ren-de-yun-dong-fan-wei-by-leetcode-solution/
class Solution1:
    """BFS, BFS使用queue再好不过"""
    def movingCount(self, m: int, n: int, k: int) -> int:
        queue = deque()
        queue.append((0,0))
        seen = set()
        while queue:
            i, j = queue.popleft()
            if (i, j) not in seen and 0<= i < m and  0<= j < n and digitsum(i, j) <= k:
                seen.add((i, j))
                if i + 1 < m:
                    queue.append((i+1, j))
                if j + 1 < n:
                    queue.append((i, j+1))
        return len(seen)

class Solution2:
    """DFS, DFS要使用递归或栈实现"""
    def movingCount(self, m: int, n: int, k: int) -> int:
        self.seen = set()
        return self.dfs(m, n, 0, 0, k)

    def dfs(self, m, n, i, j, k):
        if i >= m or j >= n or (i, j) in self.seen:
            return 0
        if digitsum(i, j) <= k:
            self.seen.add((i, j))
            return 1 + self.dfs(m, n, i+1, j, k) + self.dfs(m, n, i, j+1, k)
        return 0




class Solution3:
    """递推， DP
    递推式：vis[i][j]=(vis[i−1][j] or vis[i][j−1]) and digitSumValid
    """
    def movingCount(self, m: int, n: int, k: int) -> int:
        vis = {(0, 0)}
        for i in range(m):
            for j in range(n):
                if ((i-1, j) in vis or (i, j-1) in vis) and digitsum(i, j) <= k:
                    vis.add((i, j))
        return len(vis)


