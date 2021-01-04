import functools

class Solution:
    """注意空字符串代表一种
    Similar questions:
62. Unique Paths
70. Climbing Stairs
509. Fibonacci Number

Practice them in a row for better understanding """
    validDouble = set(str(i) for i in range(10, 27))



    @functools.lru_cache(maxsize=1000)  # 注意这里的cache是一个Solution的全局cache，所以这种方法并不太好
    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0
        l = len(s)
        if l == 0:
            return 1
        elif l == 1:
            return 1
        else:
            if s[:2] in self.validDouble:
                return self.numDecodings(s[2:]) + self.numDecodings(s[1:])
            else:
                return self.numDecodings(s[1:])


class Solution2:
    """
    https://leetcode.com/problems/decode-ways/discuss/30358/Java-clean-DP-solution-with-explanation
    使用正面思考，用dp解决，而不是使用dp把Solution1翻译下来
    dp[n]表示前n个字符的decodeWays
    那么如果s[n]和s[n-1]能组成合法的值，那么。。。 还是不行。。。。
    https://leetcode.com/problems/decode-ways/discuss/30451/Evolve-from-recursion-to-dp
    """
    validDouble = set(str(i) for i in range(10, 27))


    def numDecodings(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0

        l = len(s)
        dp = [None] * (l)
        dp[0] = 0 if s[0] == '0' else 1



if __name__ == '__main__':
    s = Solution().numDecodings
    print(s("226"))