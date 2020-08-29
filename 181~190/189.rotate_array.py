class Solution1:
    def rotate(self, nums, k):
        k = k % (len(nums))
        if k == 0:
            return nums

        for _ in range(k):
            previous = nums[-1]
            for i in range(nums):
                temp = nums[i]
                nums[i] = previous
                previous = temp


class Solution2:
    def rotate(self, nums, k):
        k = k % (len(nums))
        if k == 0:
            return nums
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)

    # [start, end]
    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

class Solution3:
    def rotate(self, nums, k):
        k = k % (len(nums))
        if k == 0:
            return nums
        count = 0
        for start in range(len(nums)):
            if count >= len(nums):
                break

            current = start
            prev = nums[start]

            next = (current + k) % len(nums)
            temp = nums[next]
            nums[next] = prev
            prev = temp
            current = next
            count += 1

            while start != current:
                next = (current + k) % len(nums)
                temp = nums[next]
                nums[next] = prev
                prev = temp
                current = next
                count += 1


if __name__ == '__main__':
    s = Solution2().rotate
    print(s([1, 2, 3, 4, 5, 6, 7], 3))