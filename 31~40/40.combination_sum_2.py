from typing import List
from copy import copy


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
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
                if remain - candidates[i] < 0:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                temp.append(candidates[i])
                self.backTrace(candidates, res, temp, remain-candidates[i], i+1)
                temp.pop()

