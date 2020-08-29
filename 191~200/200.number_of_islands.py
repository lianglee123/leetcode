class Solution:
    def numIslands(self, grid):
        count = 0
        self.n = len(grid)
        if self.n == 0:
            return 0
        self.m = len(grid[0])
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == '1':
                    self.DFSMarking(grid, i, j)
                    count += 1
        return count

    def DFSMarking(self, grid, i, j):
        if i < 0 or i >=self.n or j < 0 or j >= self.m or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.DFSMarking(grid, i+1, j)
        self.DFSMarking(grid, i-1, j)
        self.DFSMarking(grid, i, j+1)
        self.DFSMarking(grid, i, j-1)

class Solution2:
    def numIslands(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
