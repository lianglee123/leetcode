from typing import List, Set


class Solution:
    """
    回溯，注意这个回溯的迭代是在exist函数里进行的。dfs只向下回溯了word个长度个
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word, 0, set()):
                    return True
        return False

    def dfs(self, board, row, col, word: str, i, seen: Set):
        if i == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False

        if board[row][col] != word[i]:
            return False

        if (row, col) in seen:
            return False

        i += 1
        seen.add((row, col))
        res = self.dfs(board, row + 1, col, word, i, seen) or \
              self.dfs(board, row, col + 1, word, i, seen) or \
              self.dfs(board, row - 1, col, word, i, seen) or \
              self.dfs(board, row, col - 1, word, i, seen)
        seen.remove((row, col))
        return res


if __name__ == '__main__':
    s = Solution().exist
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    w1 = "ABCCED"
    w2 = "SEE"
    w3 = "ABCB"
    print(s(board, w1))
    print(s(board, w2))
    print(s(board, w3))
