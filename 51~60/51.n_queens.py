from typing import List


class Solution:
    """
    回溯就是深度优先
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for i in range(n)]
        self.backTrace(res, board, 0)
        return res

    def backTrace(self, res, board, col_index):
        if col_index == len(board):
            res.append([''.join(row) for row in board])
            return
        else:
            for i in range(len(board)):
                if self.valid(board, i, col_index):
                    board[i][col_index] = 'Q'
                    self.backTrace(res, board, col_index+1)
                    board[i][col_index] = '.'


    def valid(self, board, x, y):
        for i in range(len(board)):
            for j in range(y):
                if board[i][j] == 'Q' and (x+j==y+i or x+y==i+j or x == i):
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    res = s.solveNQueens(8)
    for i in res:
        print("-"*50)
        for j in i:
            print(j)
    print(len(res))



