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


class Solution3:
    def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
        """
        Divide-and-conquer algorithm to solve skyline problem,
        which is similar with the merge sort algorithm.
        """
        n = len(buildings)
        if n == 0:
            return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]
        left_skyline = self.getSkyline(buildings[:n//2])
        right_skyline = self.getSkyline(buildings[n//2:])
        return self.mergeSkyLine(left_skyline, right_skyline)

    def mergeSkyLine(self, left, right):
        output = []
        def updateOutput(x, y):
            if not output or output[-1][0] != x:
                output.append([x, y])
            else:
                output[-1][1] = y

        def appendSkyline(i, points, currY):
            while i < len(points):
                x, y = points[i]
                i += 1
                if currY != y:
                    updateOutput(x, y)
                    currY = y



        leftLen, rightLen = len(left), len(right)
        leftIndex, rightIndex = 0, 0
        curY, leftY, rightY = 0, 0, 0
        while leftIndex < leftLen and rightIndex < rightLen:
            leftPoint, rightPoint = left[leftIndex], right[rightIndex]
            if leftPoint[0] < rightPoint[0]:
                x, leftY = leftPoint
                leftIndex += 1
            else:
                x, rightY = rightPoint
                rightIndex += 1
            maxY = max(leftY, rightY)
            if curY != maxY:  # Y没变就不去更新output, 所以在两个高度的情况下，自动合并了。
                curY = maxY
                updateOutput(x, curY)

        appendSkyline(leftIndex, left, curY)
        appendSkyline(rightIndex, right, curY)
        return output


class Solution2:
    """
    https://leetcode-cn.com/problems/the-skyline-problem/solution/tian-ji-xian-wen-ti-by-leetcode/
    这个是leetcode官方答案的其中一个，该答案有个小问题，就是不能平滑的处理高度相等的相邻节点因此需要更改output函数
    如：有可能返回的答案为：[[2, 5],
    """
    def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
        """
        Divide-and-conquer algorithm to solve skyline problem,
        which is similar with the merge sort algorithm.
        """
        n = len(buildings)
        # The base cases
        if n == 0:
            return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]

            # If there is more than one building,
        # recursively divide the input into two subproblems.
        left_skyline = self.getSkyline(buildings[: n // 2])
        right_skyline = self.getSkyline(buildings[n // 2 :])

        # Merge the results of subproblem together.
        return self.merge_skylines(left_skyline, right_skyline)

    def merge_skylines(self, left, right):
        """
        Merge two skylines together.
        """
        def update_output(x, y):
            """
            Update the final output with the new element.
            """
            # if skyline change is not vertical -
            # add the new point
            if not output or output[-1][0] != x:
                output.append([x, y])
            # if skyline change is vertical -
            # update the last point
            else:
                output[-1][1] = y

        def append_skyline(p, lst, n, y, curr_y):
            """
            Append the rest of the skyline elements with indice (p, n)
            to the final output.
            """
            while p < n:
                x, y = lst[p]
                p += 1
                if curr_y != y:
                    update_output(x, y)
                    curr_y = y

        n_l, n_r = len(left), len(right)
        p_l = p_r = 0
        curr_y  = left_y = right_y = 0
        output = []

        # while we're in the region where both skylines are present
        while p_l < n_l and p_r < n_r:
            point_l, point_r = left[p_l], right[p_r]
            # pick up the smallest x
            if point_l[0] < point_r[0]:
                x, left_y = point_l
                p_l += 1
            else:
                x, right_y = point_r
                p_r += 1
            # max height (i.e. y) between both skylines
            max_y = max(left_y, right_y)
            # if there is a skyline change
            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y

        # there is only left skyline
        append_skyline(p_l, left, n_l, left_y, curr_y)

        # there is only right skyline
        append_skyline(p_r, right, n_r, right_y, curr_y)

        return output

if __name__ == '__main__':
    s = Solution3().getSkyline
    # b = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    # expect = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    # print("expect:", expect)
    # print(s(b))
    # assert s(b) == expect

    b = [[2, 3, 5],[3, 4, 5], [4, 5, 5]]
    print(s(b))
