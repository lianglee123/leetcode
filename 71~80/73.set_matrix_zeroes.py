class Solution(object):
    """
    真正的trick在于，上一行的更改，不能影响下一行的判断
    如果引用set记录处理过的行，会导致内存变成o(m+n)
    这里使用第一行和第一列作为 记录器。
    """
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        firstRowIsZero = False
        for v in matrix[0]:
            if v == 0:
                firstRowIsZero = True
                break

        firstColIsZero = False
        for row in matrix:
            if row[0] == 0:
                firstColIsZero = True
                break

        m, n = len(matrix), len(matrix[0])
        for r in range(1, m):
            row = matrix[r]
            for c in range(1, n):
                if row[c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if firstRowIsZero:
            for i in range(n):
                matrix[0][i] = 0

        if firstColIsZero:
            for i in range(m):
                matrix[i][0] = 0





def p_matrix(m):
    if not m:
        return
    print("*"*10)
    for row in m:
        print(row)


if __name__ == '__main__':
    s = Solution().setZeroes
    # m = [
    #     [1,1,1],
    #     [1,0,1],
    #     [1,1,1]
    # ]
    # s(m)
    # p_matrix(m)
    m = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ]
    s(m)
    p_matrix(m)