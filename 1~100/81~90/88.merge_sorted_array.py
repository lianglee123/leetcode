from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums2[j] >= nums1[i]:
                nums1[l] = nums2[j]
                j -= 1
            else:
                nums1[l] = nums1[i]
                i -= 1
            l -= 1
        while j >= 0:
            for i in range(j+1):
                nums1[i] = nums2[i]


if __name__ == '__main__':
    s = Solution().merge
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    s(nums1, 3, nums2, 3)
    print(nums1)




