from typing import *


class Solution:
    """
    该solution是我自己写的，但是在一个矩形完全包含另一个矩形的情况下，会算出错误答案， 因为overLap错了
    Solution2把第一个矩形靠左，然后就让代码少考虑了黄铎情况，这种思维值得借鉴
    """
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        print(self.recArea(A, B, C, D), self.recArea(E, F, G, H), self.overlapArea(A, B, C, D, E, F, G, H))
        return self.recArea(A, B, C, D) + self.recArea(E, F, G, H) - self.overlapArea(A, B, C, D, E, F, G, H)

    def recArea(self, A, B, C, D):
        return (C-A) * (D-B)

    def overlapArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int):
        x = self.overlapLen([A, C], [E, G])
        y = self.overlapLen([F, H], [B, D])
        print("overlap:", x, y)
        return x * y

    def overlapLen(self, line1, line2):
        """
        获取线段的重叠长度,线段用[start, end]表示
        """
        if line2[0] <= line1[0] < line2[1]:
            return min(line2[1], line1[1]) - line1[0]
        elif line2[0] < line1[1] <= line2[1]:
            return line1[1] - max(line1[0], line2[0])
        return 0

class Solution2:
    """
    https://leetcode-cn.com/problems/rectangle-area/solution/jian-dan-de-kao-lu-by-powcai/
    """
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # 调整两个矩形位置, 让第一个矩形靠最左边
        if A > E:
            return self.computeArea(E, F, G, H, A, B, C, D)
        # 没有重叠的情况
        if B >= H or D <= F or C <= E:
            return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H)
        # 重叠情况
        # 下边界
        down = max(A, E)
        # 上
        up = min(C, G)
        # 左
        left = max(B, F)
        # 右
        right = min(D, H)
        print()
        return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H) - abs(up - down) * abs(left - right)


if __name__ == '__main__':
    s = Solution().computeArea
    # print(s(-3, 0, 3, 4, 0, -1, 9, 2))
    a1 = [-2, -2, 2, 2, -1, -1, 1, 1]
    print(s(*a1))
