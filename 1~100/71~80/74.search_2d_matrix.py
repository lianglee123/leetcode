class Solution(object):
    """
    边界条件一定要搞清楚，不能通过试错法解决。
    """
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row_index = self.search_row_index(matrix, target)
        if row_index == -1:
            return False
        col_index = self.search_in_row(matrix[row_index], target)
        return col_index != -1

    def search_in_row(self, row, target):
        top, bottom = 0, len(row)-1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if row[mid] < target:
                top = mid + 1
                pass
            elif row[mid] > target:
                bottom = mid - 1
            else:
                return mid
        return -1

    def search_row_index(self, m, target):
        """
        top 上面的都小于target(不包括top)
        bottom 下面的都大于target(不包括bottom)
        所以top, bottom不能重叠
        :param m:
        :param target:
        :return:
        """
        top, bottom = 0, len(m)-1
        if m[top][0] > target:
            return -1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            # print("mide: ", mid)
            if m[mid][0] < target:
                top = mid + 1
            elif m[mid][0] > target:
                bottom = mid - 1
            else:
                return mid
        if bottom == len(m) - 1:
            if m[len(m)-1][len(m[0])-1] < target:
                return -1
        return bottom



class Solution2:
    """
    https://leetcode.com/problems/search-a-2d-matrix/discuss/26220/Don't-treat-it-as-a-2D-matrix-just-treat-it-as-a-sorted-list
    """
    pass

if __name__ == '__main__':
    s = Solution()

    # m = [
    #     [1],
    #     [2],
    #     [3],
    #     [4],
    #     [5],
    # ]
    # print(s.search_row_index(m, 6))
    # print(s.search_row_index(m, 0))
    # print(s.search_row_index(m, 2))
    # print(s.search_row_index(m, 5))
    # print(s.search_row_index(m, 1))

    # r = [0, 1, 2, 3, 4]
    # print(s.search_in_row(r, 6) == -1)
    # print(s.search_in_row(r, 0) == 0)
    # print(s.search_in_row(r, 2) == 2)
    # print(s.search_in_row(r, 4) == 4)
    # print(s.search_in_row(r, -1) == -1)
    #
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3

    # print(s.search_row_index(matrix, 1) == 0)
    # print(s.search_row_index(matrix, 3) == 0)
    # print(s.search_row_index(matrix, 10) == 1)
    # print(s.search_row_index(matrix, 20) == 1)
    # print(s.search_row_index(matrix, 23) == 2)
    # print(s.search_row_index(matrix, 34) == 2)

    print(s.search_in_row(matrix[0], -1)== -1)
    print(s.search_in_row(matrix[0], 1) == 0)
    print(s.search_in_row(matrix[0], 3) == 1)
    print(s.search_in_row(matrix[0], 5) == 2)
    print(s.search_in_row(matrix[0], 7) == 3)
    print(s.search_in_row(matrix[0], 9) == -1)