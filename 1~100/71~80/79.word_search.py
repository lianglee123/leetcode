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


class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False


STEPS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

class Solution3:
    def exist(self, board: List[List[str]], word: str) -> bool:
        S = word
        L = len(S)
        if L<=0: return True
        W = board
        N = len(W)
        if N<=0: return False
        M = len(W[0])
        if M<=0: return False
        B = [[True]*M for _ in range(N)]

        def DFS(i, j, c):
            if c+1>=L: return True

            B[i][j] = False
            for di, dj in STEPS:
                ni = i+di
                nj = j+dj
                if 0<=ni<N and 0<=nj<M and B[ni][nj] and W[ni][nj]==S[c+1]:
                    if DFS(ni, nj, c+1): return True
            B[i][j] = True

            return False

        for i in range(N):
            for j in range(M):
                if W[i][j]==S[0]:
                    if DFS(i, j, 0): return True

        return False

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
