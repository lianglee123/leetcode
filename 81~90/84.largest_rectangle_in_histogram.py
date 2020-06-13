class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        ans = 0
        i = 0
        nums = [h for h in heights]
        nums.append(0)   # 这一行是必须的，否则无法处理单调递增的情况。俩如[1, 2, 3, 4, 5]
        while i < len(nums):
            if not stack or nums[i] > nums[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                h = nums[stack.pop()]
                if not stack:
                    width = 1
                else:
                    width = i - stack[-1] - 1
                ans = max(ans, h * width)
        return ans

class Solution2:
    def largestRectangleArea(self, heights):
        stack = []
        i = 0
        maxArea = 0
        while i <= len(heights):
            h = 0 if i == len(heights) else heights[i]
            if not stack or h >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                curHeight = heights[stack.pop()]
                rightBoundary = i - 1
                leftBoundary = stack[-1] + 1 if stack else 0
                width = rightBoundary - leftBoundary + 1
                maxArea = max(maxArea, curHeight * width)
        return maxArea


class Solution3:
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


if __name__ == '__main__':
    s = Solution2().largestRectangleArea
    # print(s([2,1,5,6,2,3])==10)
    # print(s([1]) == 1)
    print(s([1, 1]) == 2)