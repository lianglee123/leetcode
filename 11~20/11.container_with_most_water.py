from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_ptr = 0
        right_ptr = len(height) - 1
        while right_ptr > left_ptr:
            area = (right_ptr - left_ptr) * min(height[right_ptr], height[left_ptr])
            max_area = max(area, max_area)
            if (height[left_ptr] <= height[right_ptr]):
                left_ptr += 1
            else:
                right_ptr -= 1
        return max_area

class Solution2:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_ptr = 0
        right_ptr = len(height) - 1
        while right_ptr > left_ptr:
            right_h = height[right_ptr]
            left_h = height[left_ptr]
            area = (right_ptr - left_ptr) * min(right_h, left_h)
            max_area = max(area, max_area)
            if (left_h <= right_h):
                left_ptr += 1
            else:
                right_ptr -= 1
        return max_area

