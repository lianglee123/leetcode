class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return n
        return self.dfs(1, n, {})

    def dfs(self, start, end, memo):
        if (start, end) in memo:
            return memo[(start, end)]
        if start > end:
            memo[(start, end)] = 1
            return 1
        ans = 0
        for i in range(start, end+1):
            left = (start, i-1, memo)
            right = (i+1, end, memo)
            ans += (self.dfs(*left) * self.dfs(*right))
        memo[(start, end)] = ans
        return ans



class Solution2:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return n
        return self.dfs(1, n, {})

    def dfs(self, start, end, memo):
        s = end - start
        if s in memo:
            return memo[s]
        if s < 0:
            memo[s] = 1
            return 1
        ans = 0
        for i in range(start, end+1):
            left = (start, i-1, memo)
            right = (i+1, end, memo)
            ans += (self.dfs(*left) * self.dfs(*right))
        memo[s] = ans
        return ans


if __name__ == '__main__':
    s = Solution2().numTrees
    print(s(3))