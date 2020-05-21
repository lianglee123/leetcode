class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        zero_ord = ord('0')
        multi_nums = [0] * (len(num1) + len(num2))
        for i, n1_char in enumerate(reversed(num1)):
            for j, n2_char in enumerate(reversed(num2)):
                n1 = ord(n1_char) - zero_ord
                n2 = ord(n2_char) - zero_ord
                multi_nums[i+j] += (n1 * n2)
                multi_nums[i+j+1] += multi_nums[i+j] // 10
                multi_nums[i+j] = multi_nums[i+j] % 10
        multi_nums.reverse()
        res = ''
        for n in multi_nums:
            res += str(n)
        res = res.lstrip("0")
        if res:
            return res
        else:
            return '0'


if __name__ == '__main__':
    s = Solution().multiply
    s('123', "32")
    s('666', "666")