

class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        n1, n2 = 1, 2
        for i in range(n-2):
            n1, n2 = n2,  n1 + n2
        return  n2


if __name__ == '__main__':
    s = Solution().climbStairs
    print(s(4))

