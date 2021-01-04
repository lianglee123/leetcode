from typing import List


class Solution:
    """
    回溯就是深度优先
    """

    def totalNQueens(self, n: int) -> int:
        self.count = 0
        board = [['.'] * n for i in range(n)]
        self.backTrace(board, 0)
        return self.count

    def backTrace(self, board, col_index):
        if col_index == len(board):
            self.count += 1
            return
        else:
            for i in range(len(board)):
                if self.valid(board, i, col_index):
                    board[i][col_index] = 'Q'
                    self.backTrace(board, col_index+1)
                    board[i][col_index] = '.'


    def valid(self, board, x, y):
        for i in range(len(board)):
            for j in range(y):
                if board[i][j] == 'Q' and (x+j==y+i or x+y==i+j or x == i):
                    return False
        return True


class Solution2:
    """
    回溯就是深度优先
    一个主要的信息是\对角线上的元素x-y是相等的
/对角线上x-y是相等的

    """

    def totalNQueens(self, n: int) -> int:
        self.count = 0
        cols = [False] * n
        d1 = [False] * 2 * n  # diagonals \
        d2 = [False] * 2 * n  # diagonals /
        self.backTrace(0, cols, d1, d2, n)
        return self.count

    def backTrace(self, row, cols, d1, d2, n):
        if row == n:
            self.count += 1
            return
        for col in range(0, n):
            id1 = col-row
            id2 = col + row
            if cols[col] or d1[id1] or d2[id2]:
                continue

            cols[col] = True
            d1[id1] = True
            d2[id2] = True
            self.backTrace(row+1, cols, d1, d2, n)
            cols[col] = False
            d1[id1] = False
            d2[id2] = False



if __name__ == '__main__':
    s = Solution()
    res = s.totalNQueens(8)
    print(res)


