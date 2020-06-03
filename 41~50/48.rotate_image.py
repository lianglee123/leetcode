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


class Solution2:
    """
    https://mp.weixin.qq.com/s?__biz=MzI2NjI5MzU2Nw==&mid=2247485331&idx=1&sn=ca09244eaa8de904844fd5e8ca7cd407&chksm=ea911fc3dde696d5077415e9ad97988a895a2354e72b989cfa2772978b07536652020c303aba&scene=126&sessionid=1591103755&key=b7b0d71aeeec04a335b60e3da584042475a8d92e68de77f891a4a0b7dc6cf3dd64ae87eb39ad131d75952094f02ce24cafa629a01db9ae6ecf923b7400f31b89e9ee8ca95f85df7a0073cafeb2e951e9&ascene=1&uin=MjcxNDI2ODQ0Mg%3D%3D&devicetype=Windows+10+x64&version=62090070&lang=zh_CN&exportkey=ASzcazw%2FDOH5lKodL6iXVEk%3D&pass_ticket=MM15MA1iWkPm6dGYW882Mg6c%2FrfX9NWGvArLE5uT7j2CBMTjLv4rVuuaaqs%2BJlws
    """

    def rotate(self, matrix):
        l = len(matrix)
        x, y = 0, l - 1
        while x < y:
            s, e = x, y   # 这里引用了变量e，很巧妙。
            while s < y:
                matrix[x][s], matrix[s][y], matrix[y][e], matrix[e][x] = \
                    matrix[e][x], matrix[x][s], matrix[s][y], matrix[y][e],
                s += 1
                e -= 1
            x += 1
            y -= 1



def p(m):
    print("*"*20)
    for i in m:
        print(i)
    print("*"*20)

if __name__ == '__main__':
    s = Solution2()

    # m = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]
    m = [
        [1, 2, 3, "A"],
        [4, 5, 6, "A"],
        [7, 8, 9, "A"],
        [10, 11, 12, "A"]
    ]
    m = [
        ["A1"] * 4,
        ["A2"] * 4,
        ["A3"] * 4,
        ["A4"] * 4,
    ]
    # m = [
    #     [1, 2],
    #     [3, 4]
    # ]
    p(m)
    s.rotate(m)
    p(m)