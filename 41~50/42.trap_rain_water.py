class Solution1:
    """
    这个题的关键是转变思路，把整体求容积，变成一个一个求小格的容积。
    那么小格子的容积为min(左边最大值, 右边最大值) - 格子高度。
    """
    def trap(self, height):
        res = 0
        for i in range(len(height)):
            l = max(height[0:i+1])
            r = max(height[i:])
            res += min(l, r) - height[i]
            print(i, "L:", l, "R:", r, "Trap:", min(l, r) - height[i])
        return res


class Solution2:
    """
    从第一个Solution显而易见的可以进化到dp，使用dp_l[i]表示i之前的最大致(包括i)，dp_r[i]表示i右边的最大值（包括i)
    """
    def trap(self, height):
        if not height:
            return 0
        l = len(height)
        dp_l = [0]*l
        dp_l[0] = height[0]
        for i in range(1, len(height)):
            dp_l[i] = max(dp_l[i-1], height[i])
        dp_r = [0]*l
        dp_r[-1] = height[-1]
        for i in range(l-2, -1, -1):
            dp_r[i] = max(dp_r[i+1], height[i])
        res = 0
        for i in range(len(height)):
            l = dp_l[i]
            r = dp_r[i]
            res += min(l, r) - height[i]
        return res


class Solution3:
    """
    双指针
    边迭代，边找最大值，并计算
    """
    def trap(self, height):
        pass



if __name__ == '__main__':
    s = Solution2().trap
    print(s([0,1,0,2,1,0,1,3,2,1,2,1]) == 6)