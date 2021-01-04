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


class Solution3:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]
class Solution4:
    """
    直接使用卡塔兰数
    """
    def numTrees(self, n):
        pass




if __name__ == '__main__':
    s = Solution2().numTrees
    print(s(3))