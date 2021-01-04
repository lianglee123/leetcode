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


class Solution2:
    """
    使用栈
    https://leetcode-cn.com/problems/longest-valid-parentheses/solution/shou-hua-tu-jie-zhan-de-xiang-xi-si-lu-by-hyj8/
    查看笨猪爆破组的解法
    """
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stx = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stx.append(i)
            else:
                stx.pop()
                if stx:
                    ans = max(ans, i- stx[-1])
                else:
                    stx.append(i)
        return ans



if __name__ == '__main__':
    s = Solution().longestValidParentheses
    # print(s(')()))('))
    print(s("()(())"))
