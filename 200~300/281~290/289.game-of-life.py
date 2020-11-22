from typing import *


class Solution:
    """
    生命游戏
    1: live
    0: dead
    2: live->dead
    3: dead->live
    """
    def gameOfLift(self, board):
        if not board or not board[0]:
            return
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 0:
                    if self.countAliveAround(i, j, board) == 3:
                        board[i][j] = 3
                elif board[i][j] == 1:
                    cnt = self.countAliveAround(i, j, board)
                    if cnt < 2:
                        board[i][j] = 2
                    elif cnt in (2, 3):
                        pass
                    else:
                        board[i][j] = 2

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1



    def countAliveAround(self, i, j, board):
        count = 0
        for iStep in (-1, 0, 1):
            for jStep in (-1, 0, 1):
                if iStep == 0 and jStep == 0:
                    continue
                nextI = i + iStep
                nextJ = j + jStep
                if not self.validPos(nextI, nextJ, board):
                    continue
                if board[nextI][nextJ] in (1, 2):
                    count += 1
        return count

    def validPos(self, i, j, board):
        return 0 <= i < len(board) and 0 <= j < len(board[0])