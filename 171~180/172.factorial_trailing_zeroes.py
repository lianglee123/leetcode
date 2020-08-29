class Solution:
    """
    其实就是统计n中质因子5的个数,我们逐层统计
    """
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            res += n//5
            n = n//5
        return res


