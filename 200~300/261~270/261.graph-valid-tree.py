from typing import *

from collections import defaultdict
class Solution:
    """
    DFS
    https://www.cnblogs.com/grandyang/p/5257919.html
    """
    def validTree(self, n, edges):
        g = defaultdict(set)
        for e in edges:
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        seen = set()
        if not self.dfs(g, seen, 0, -1):
            return False
        return len(seen) == n


    def dfs(self, g, seen, cur, pre):  # pre这个变量的含义是为了防止回到上一个节点
        if cur in seen:
            return False
        seen.add(cur)
        for n in g[cur]:
            if n != pre:
                if not self.dfs(g, seen, a, cur):
                    return False
        return True

from collections import deque


class Solution2:
    """
    BFS
    """
    def validTree(self, n, edges):
        g = defaultdict(set)
        for e in edges:
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        q = deque()
        seen = set()
        q.appendleft(0)
        while q:
            t = q.pop()
            for n in g[t]:
                if n in seen:
                    return False
                seen.add(n)
                g[n].remove(t)  # 防止回到上一个焦点，但是修改了graph, 所以通用
                q.appendleft(n)
        return len(seen) == n
