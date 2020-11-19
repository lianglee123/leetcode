from typing import *


from collections import defaultdict, deque

class Solution:
    """
    https://blog.csdn.net/qq_37821701/article/details/108807236
    """
    def alienOrder(self, words: List[str]) -> str:
        indegrees = {c: 0 for c in ''.join(words)}
        adj_list = defaultdict(set)
        for first, second in zip(words, words[1:]):
            for c, d in zip(first, second):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        indegrees[d] += 1
                    break
        q = deque()
        for k, v in indegrees.items():
            if v == 0: q.append(k)

        ans = []
        while q:  # 这种其实是BFS， q里保存里的都是零入度的节点， 如果有环，有环的部分是没有办法被遍历的
            c = q.popleft()
            ans.append(c)
            for d in adj_list[c]:
                indegrees[d] -= 1
                if indegrees[d] == 0:
                    q.append(d)

        if len(ans) < len(indegrees):
            return ''
        return ''.join(ans)
