from typing import *


class Solution:
    """
    https://juejin.im/post/5ce974f151882530e807e21c
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                self.dfs(board, i, j)

        for i in range(1, len(board)-1):
            for j in [0, len(board[0])-1]:
                self.dfs(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'



    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) \
                or  board[i][j] == "X" or board[i][j] == "#":
            return
        board[i][j] = "#"
        self.dfs(board, i - 1, j)
        self.dfs(board, i+1, j)
        self.dfs(board, i, j+1)
        self.dfs(board, i, j-1)


