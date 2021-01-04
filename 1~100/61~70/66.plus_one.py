from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            carry, digits[i] = divmod(digits[i]+1, 10)
            if carry == 0:
                return digits
        if carry != 0:
            digits.insert(0, carry)
        return digits


if __name__ == '__main__':
    s = Solution().plusOne
    print(s([1, 2, 3]))
    print(s([4, 3, 2, 1]))
    print(s([9, 9, 9, 9]))