from typing import List


def none(*args, **kwargs):
    return


p = print


class Solution:
    """
    搞不懂，这个为什么错了
    """
    MAYBE = [str(i) for i in range(1, 10)]

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.backTrace(board, 0, 0)

    def backTrace(self, board, row_start, col_start) -> bool:
        # print("row_start, col_start", row_start, col_start )
        for i in range(row_start, len(board)):
            for j in range(col_start, len(board[0])):
                if board[i][j] == '.':
                    next_j = 0 if j == 8 else j + 1
                    next_i = i+1 if next_j == 0 else i
                    print('i, j: ', i, j, "next i, j: ", next_i, next_j)
                    for c in Solution.MAYBE:
                        if not self.valid(board, i, j, c):
                            continue
                        board[i][j] = c
                        if self.backTrace(board, next_i, next_j):
                            return True
                        else:
                            board[i][j] = '.'
                    return False
        return True

    def valid(self, board, row, col, c):
        # p("valid row, col", row, col)
        valid_nums = set(Solution.MAYBE)
        for i in range(len(board)):
            # print("board[row]", board[row])
            if board[row][i] in valid_nums:
                valid_nums.remove(board[row][i])

            if board[i][col] in valid_nums:
                valid_nums.remove(board[i][col])

            x, y = self.cube_ele_position(row, col, i)
            # p(x, y)
            if board[x][y] in valid_nums:
                valid_nums.remove(board[x][y])
        return c in valid_nums

    def cube_ele_position(self, row, col, i):
        # p("-" * 10)
        # p("row: ", row, "col: ", col, )
        cube_row = row // 3
        cube_col = col // 3
        # p("cube_row: ", cube_row, "cube_col: ", cube_col, )
        ele_row_in_cube = i // 3
        ele_col_in_cube = i % 3
        # p("ele_row_in_cube: ", ele_row_in_cube, "ele_col_in_cube: ", ele_col_in_cube, )

        ele_row_in_board = cube_row * 3 + ele_row_in_cube
        ele_col_in_board = cube_col * 3 + ele_col_in_cube
        # p("ele_row_in_board: ", ele_row_in_board, "ele_col_in_board: ", ele_col_in_board)
        # p("-" * 10)
        return ele_row_in_board, ele_col_in_board


def test1():
    s = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "."]]
    # print(s.cube_ele_position(0, 2, 2))
    # p(s.solveSudoku(board))
    # for i in board:
    #     print(i)
    board = [["."]*9 for i in range(9)]
    # print(board)
    for row in board:
        print(row)
    s.solveSudoku(board)
    for row in board:
        print(row)

def test2():
    s = Solution()
    b = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","."]]
    s.solveSudoku(b)
    for r in b:
        print(r)


if __name__ == '__main__':
    test2()