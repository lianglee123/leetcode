class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        h, w = len(matrix), len(matrix[0])
        m = [[0]*w for _ in range(h)]
        for j in range(h):
            for i in range(w):
                if matrix[j][i] == '1':
                    m[j][i] = m[j-1][i] + 1
        return max(self.largestRectangleArea(row) for row in m)

    def largestRectangleArea(self, heights):
        heights.append(0)
        stack, size = [], 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                size = max(size, h*w)
            stack.append(i)
        return size


class Solution2:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        h, w = len(matrix), len(matrix[0])
        res = 0
        height = [0] * w
        for row in matrix:
            for i in range(w):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            res = max(0, self.largestRectangleArea(height))
        return res

    def largestRectangleArea(self, heights):
        heights.append(0)
        stack, size = [], 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                size = max(size, h*w)
            stack.append(i)
        heights.pop()
        return size
