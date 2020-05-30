from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.reverse_up_to_down(matrix)
        self.swap_symmetry(matrix)

    def swap_symmetry(self, matrix):
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reverse_up_to_down(self, maxtrix):
        for i in range(len(maxtrix)//2):
            j = len(maxtrix) - i - 1
            self.swap_line(maxtrix, i, j)


    def swap_line(self, maxtrix, i, j):
        maxtrix[i], maxtrix[j] = maxtrix[j], maxtrix[i]


def p(m):
    print("*"*20)
    for i in m:
        print(i)
    print("*"*20)

if __name__ == '__main__':
    s = Solution()

    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s.reverse_up_to_down(m)
    p(m)