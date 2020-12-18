from functools import lru_cache


class Solution:
    """
    原理级别的方法：深度优先的搜索。但是复杂度是3^min(len(w2), len(w1))（搜索树的大小)
    当最小长度为22时，搜素节点数量就变成百亿了。所以，理所当然引出了各种优化算法，包括不限于DP
    """
    def minDistance(self, w1: str, w2: str) -> int:
        if len(w1) == 0:
            return len(w2)
        if len(w2) == 0:
            return len(w1)

        if w1[-1] == w2[-1]:
            return self.minDistance(w1[:-1], w2[:-1])
        else:
            replace_distance = self.minDistance(w1[:-1], w2[:-1]) + 1
            add_distance = self.minDistance(w1[:-1], w2) + 1
            del_distance = self.minDistance(w1, w2[:-1]) + 1
            return min(replace_distance, add_distance, del_distance)


class Solution2:
    """
    基于上面的方法，使用万能DP法(cache)，内存是len(m) * len(n)
    """
    @lru_cache(maxsize=None)
    def minDistance(self, w1: str, w2: str) -> int:
        if len(w1) == 0:
            return len(w2)
        if len(w2) == 0:
            return len(w1)

        if w1[-1] == w2[-1]:
            return self.minDistance(w1[:-1], w2[:-1])
        else:
            replace_distance = self.minDistance(w1[:-1], w2[:-1]) + 1
            add_distance = self.minDistance(w1[:-1], w2) + 1
            del_distance = self.minDistance(w1, w2[:-1]) + 1
            return min(replace_distance, add_distance, del_distance)



if __name__ == '__main__':
    s = Solution().minDistance
    w1, w2 = "dinitrophenylhydrazine", "benzalphenylhydrazone"
    print(s(w1, w2) == 7)
