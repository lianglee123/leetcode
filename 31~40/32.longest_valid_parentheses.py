class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        dp = [0] * len(s)
        res = 0
        for i, c in enumerate(s):
            if i == 0:
                continue
            if c == '(':
                dp[i] = 0
            else:
                j = i - dp[i-1] - 1
                if j < 0:
                    continue
                if s[j] == '(':
                    dp[i] = dp[i-1] + 2 + dp[j-1] if j-1 >= 0 else dp[i-1] + 2
                else:
                    dp[i] = 0
            res = max(dp[i], res)
        return res


if __name__ == '__main__':
    s = Solution().longestValidParentheses
    # print(s(')()))('))
    print(s("()(())"))
