from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        res = []
        while i < len(intervals):
            cur_inter = intervals[i]
            i+=1
            while i < len(intervals) and cur_inter[1] >= intervals[i][0]:
                cur_inter = self.mergeTwo(cur_inter, intervals[i])
                i += 1
            res.append(cur_inter)

        return res


    def mergeTwo(self, a, b):
        return [min(a[0], b[0]), max(a[1], b[1])]


def t():
    i = 0
    while i < 5:
        print("less 5")
        i += 1
    else:
        print("out")

if __name__ == '__main__':
    s = Solution().merge
    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    # print(s(intervals))
    # print(s([[1, 4], [4, 5]]))
    print(s([[1, 4], [0, 0]]))