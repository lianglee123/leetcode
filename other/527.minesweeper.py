from typing import *
from collections import deque

class Solution1:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]:
            return board
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        else:
            self.initDirections()
            self.board = board
            self.dfs(x, y)
            return board


    def dfs(self, r, c):
        if self.board[r][c] in ('X', 'M'):
            return
        elif self.board[r][c] == 'E':
            aroundMineCount = self.getAroundMine(r, c)
            if aroundMineCount:
                self.board[r][c] = str(aroundMineCount)
                return
            self.board[r][c] = 'B'
            for dX, dY in self.directions:
                nextR, nextC = r + dX, c + dY
                if self.positionValid(nextR, nextC) and self.board[nextR][nextC] == 'E':
                    self.dfs(nextR, nextC)
        else:
            return

    def getAroundMine(self, r, c):
        res = 0
        for dX, dY in self.directions:
            nextR, nextC = r + dX, c + dY
            if self.positionValid(nextR, nextC):
                res += self.board[nextR][nextC] in ('M', 'X')
        return res

    def positionValid(self, r, c):
        return 0 <= r < len(self.board) and 0 <= c < len(self.board[0])


    def initDirections(self):
        self.directions = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                self.directions.append([x, y])

class Solution2:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]:
            return board
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        else:
            self.initDirections()
            self.board = board
            self.bfs(x, y)
            return board


    def bfs(self, r, c):
        queue = deque()
        queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            if self.board[r][c] in ('X', 'M'):
                continue
            elif self.board[r][c] == 'E':
                aroundMineCount = self.getAroundMine(r, c)
                if aroundMineCount:
                    self.board[r][c] = str(aroundMineCount)
                    continue
                self.board[r][c] = 'B'
                for dX, dY in self.directions:
                    nextR, nextC = r + dX, c + dY
                    if self.positionValid(nextR, nextC) and self.board[nextR][nextC] == 'E':
                        queue.append((nextR, nextC))

    def getAroundMine(self, r, c):
        res = 0
        for dX, dY in self.directions:
            nextR, nextC = r + dX, c + dY
            if self.positionValid(nextR, nextC):
                res += self.board[nextR][nextC] in ('M', 'X')
        return res

    def positionValid(self, r, c):
        return 0 <= r < len(self.board) and 0 <= c < len(self.board[0])


    def initDirections(self):
        self.directions = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                self.directions.append([x, y])



if __name__ == '__main__':
    from utils import pprint
    boards = [['E', 'E', 'E', 'E', 'E'],
              ['E', 'E', 'M', 'E', 'E'],
              ['E', 'E', 'E', 'E', 'E'],
              ['E', 'E', 'E', 'E', 'E']]
    s = Solution2().updateBoard
    pprint(s(boards, [3, 0]))
    boards2 = [['B', '1', 'E', '1', 'B'],
               ['B', '1', 'M', '1', 'B'],
               ['B', '1', '1', '1', 'B'],
               ['B', 'B', 'B', 'B', 'B']]

    pprint(s(boards2, [1, 2]))
