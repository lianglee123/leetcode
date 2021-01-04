from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[0]*col for i in range(row)]
        max_int = float('inf')
        for r in range(row):
            for c in range(col):
                if r==0 and c == 0:
                    dp[0][0] = grid[0][0]
                    continue
                left = dp[r][c-1] if c-1 >= 0 else float('inf')
                right = dp[r-1][c] if r-1 >= 0 else float('inf')
                dp[r][c] = min(left, right) + grid[r][c]
        return dp[row-1][col-1]


if __name__ == '__main__':
    s = Solution().minPathSum
    i = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    print(s(i))
