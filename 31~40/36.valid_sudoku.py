from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row_set = set()
            col_set = set()
            cube_set = set()
            for j in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    else:
                        row_set.add(board[i][j])

                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                    else:
                        col_set.add(board[j][i])

                #  total 9 cube， 3*3
                cube_row = i // 3
                cube_col = i % 3
                ele_row_in_cube = j // 3
                ele_col_in_cube = j % 3
                ele_row_in_board = cube_row * 3 + ele_row_in_cube
                ele_col_in_board = cube_col * 3 + ele_col_in_cube
                ele = board[ele_row_in_board][ele_col_in_board]
                if ele != '.':
                    if ele in cube_set:
                        return False
                    else:
                        cube_set.add(ele)
        return True


class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        base_index = ord('0') + 1
        for i in range(len(board)):
            row_list = [False] * 10
            col_list = [False] * 10
            cube_list = [False] * 10
            for j in range(len(board)):
                if board[i][j] != '.':
                    row_ele = ord(board[i][j]) - base_index
                    if row_list[row_ele]:
                        return False
                    else:
                        row_list[row_ele] = True

                if board[j][i] != '.':
                    col_ele = ord(board[j][i]) - base_index
                    if col_list[col_ele]:
                        return False
                    else:
                        col_list[col_ele] = True

                #  total 9 cube， 3*3
                cube_row = i // 3
                cube_col = i % 3
                ele_row_in_cube = j // 3
                ele_col_in_cube = j % 3
                ele_row_in_board = cube_row * 3 + ele_row_in_cube
                ele_col_in_board = cube_col * 3 + ele_col_in_cube
                if board[ele_row_in_board][ele_col_in_board] != '.':
                    ele = ord(board[ele_row_in_board][ele_col_in_board]) - base_index
                    if cube_list[ele]:
                        return False
                    else:
                        cube_list[ele] = True
        return True


if __name__ == '__main__':
    s = Solution2().isValidSudoku
    board = [[".",".","4",".",".",".","6","3","."],
             [".",".",".",".",".",".",".",".","."],
             ["5",".",".",".",".",".",".","9","."],
             [".",".",".","5","6",".",".",".","."],
             ["4",".","3",".",".",".",".",".","1"],
             [".",".",".","7",".",".",".",".","."],
             [".",".",".","5",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."]]
    print(s(board))