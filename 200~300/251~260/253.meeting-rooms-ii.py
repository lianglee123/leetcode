from typing import *

import heapq


class Solution:
    """
    和天际线问题的解法相同
    """
    def minMeetingRooms(self, intervals):
        if len(intervals) <= 1:
            return len(intervals)
        intervals.sort(key=lambda x: x[0])
        heap = []
        res = 1
        for l, r in intervals:
            while heap and heap[0][1] <= l: # 当前位置已结束
                heapq.heappop(heap)
            heapq.heappush(heap, (l, r))
            res = max(res, len(heap))
        return res



class Solution1:
    """
    https://www.cnblogs.com/grandyang/p/5244720.html
    这个不一定对
    """
    def minMeetingRooms(self, intervals):
        if len(intervals) <= 1:
            return len(intervals)
        a = []
        for interval in intervals:
            a.append((interval[0], 's'))
            a.append((interval[1], 'e'))

        res = 0
        t = 0
        a.sort(key=lambda x: x[0])
        for i in a:
            if i[1] == 's':
                t += 1
            else:
                t -= 1
            res = max(res, t)
        return t


