from typing import List


class Solution:
    """
    回溯
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backTrace(res, 1, n+1, [], k)
        return res

    def backTrace(self, res, start, end, temp, k):
        if len(temp) == k:
            res.append([i for i in temp])
        else:
            for n in range(start, end):
                temp.append(n)
                self.backTrace(res, n+1, end, temp, k)
                temp.pop()



def p_matrix(m):
    if not m:
        return
    print("*"*10)
    for row in m:
        print(row)


if __name__ == '__main__':
    s = Solution().combine
    p_matrix(s(4, 2))