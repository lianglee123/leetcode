from typing import List
from copy import copy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        # candidates.sort()  在没有重复元素的情况下不用排序。
        res = []
        self.backTrace(candidates, res, [], target, 0)
        return res


    def backTrace(self, candidates, res, temp, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            res.append(copy(temp))
        else:
            for i in range(start, len(candidates)):
                temp.append(candidates[i])
                # not i+1, because we can use i mutiple times
                self.backTrace(candidates, res, temp, remain-candidates[i], i+1)
                temp.pop()
