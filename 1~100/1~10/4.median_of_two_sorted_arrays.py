from typing import List

MIN_VALUE = float("-inf")
MAX_VALUE = float("inf")

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1) > len(nums2)):
            return self.findMedianSortedArrays(nums2, nums1)

        x = len(nums1)
        y = len(nums2)
        low, high = 0, x
        even = (x + y)%2 == 0

        while low <= high:
            partition_x = (low + high) // 2
            partition_y = (x + y + 1)//2 - partition_x

            max_left_x =  MIN_VALUE if partition_x == 0 else nums1[partition_x-1]
            min_right_x = MAX_VALUE if partition_x == x else nums1[partition_x]

            max_left_y = MIN_VALUE if partition_y == 0 else nums2[partition_y-1]
            min_right_y = MAX_VALUE if partition_y == y else nums2[partition_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if even:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_y, max_left_x)
            elif max_left_x > min_right_y:
                high = partition_x - 1
            else:
                low = partition_x + 1

        raise ValueError("can not find median")

if __name__ == '__main__':
    s = Solution().findMedianSortedArrays
    print(s( [7, 7, 7], [6, 6, 6, 6, 6, 6]))

