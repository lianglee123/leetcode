from typing import *

class Solution:
    """
    从dp的角度，双重dp
    https://blog.csdn.net/qq508618087/article/details/50863010
    """
    def numWays(self, n, k):
        if not n or not k:
            return 0
        dp1 = [0] * (n+1)  # 和前一个染一样的色，如果选择和前一个染一样的色，那么他的前一个一定不能选择染同样的色
        dp2 = [0] * (n+1)  # 和前一个染不一样的色。
        dp1[1] = 0
        dp2[2] = k
        for i in range(2, n+1):
            dp1[i] = dp2[i-1]
            dp2[i] = (dp1[i-1] + dp2[i-1]) * (k - 1)
        return dp1[n] + dp2[n]


class Solution2:
    """
    压缩dp状态
    """
    def numWays(self, n, k):
        if not n or not k:
            return 0
        same = 0
        diff = k
        for i in range(2, n+1):
            same, diff = diff, (same + diff) * (k-1)
        return same + diff
