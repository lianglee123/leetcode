from typing import List


class Solution:
    def generateParenthesis(self, n):
        res = []
        self.back_trace(0, n, 0, n, '', res)
        return res

    def back_trace(self, l_count, l_remainder, r_count, r_remainder, prefix, res: List):
        if r_remainder == 0:
            res.append(prefix)
            return
        if l_remainder > 0:
            self.back_trace(l_count+1, l_remainder-1, r_count, r_remainder, prefix+"(", res)

        if r_remainder > 0:
            if l_count > r_count:
                self.back_trace(l_count, l_remainder, r_count+1, r_remainder-1, prefix+")", res)



if __name__ == '__main__':
    s = Solution().generateParenthesis
    print(s(3))