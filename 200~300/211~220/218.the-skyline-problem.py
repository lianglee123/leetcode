from typing import *

import heapq

class Solution:
    """
    天际线的点，其实就是沿x轴扫描，高度有变化的点
    """
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # point 代表的每个位置上高度和和范围。
        # 优先L, -H, R的的顺序排序。L最小的排到前面，L相同，把H最大的排到最前面, H也相同，把R最小的排到前面
        # 加上(R, 0, 0)是代表那些高度位零的地方, 注意(R, 0, 0)的right值为0, 是因为计算天际点的时候只需要知道这里有个结束的转折点就行了，
        # 不用考虑他的长度
        points = [(L, -H, R) for L, R, H in buildings] + [(R, 0, 0) for R in set(r for _, r, _ in buildings)]
        points.sort()
        heap = []  # heap的堆顶是(当前位置的最大高度, 高度结束位置(r))
        res = [[0, 0]]
        print(points)
        for l, h, r in points:
            print("#"*30)
            print("point:", (l, h, r))
            print("res:", res)
            print("before pop:", l, "--->", heap)
            while heap and heap[0][1] <= l: # 当前高度的有效位置已经结束
                heapq.heappop(heap)
            print("after pop:", l, "--->", heap)
            heapq.heappush(heap, (h, r))
            print("after push:", l, "--->", heap)
            if res[-1][1] != -heap[0][0]: # 随着l的变化，有效高度已经变化
                res.append([l, -heap[0][0]])
            print("res: ", res)
        return res[1:]


if __name__ == '__main__':
    s = Solution().getSkyline
    b = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    expect = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    print("expect:", expect)
    print(s(b))
    assert s(b) == expect

