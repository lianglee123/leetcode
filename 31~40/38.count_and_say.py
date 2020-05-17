class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        last = self.countAndSay(n-1)
        s, e = 0, len(last) - 1
        res = ''
        while s <= e:
            char = last[s]
            s += 1
            count = 1
            while s <= e and last[s] == last[s-1]:
                s += 1
                count += 1
            res += (str(count) + char)
        return res


if __name__ == '__main__':
    s = Solution().countAndSay
    s(1)
    print(s(2))
    print(s(3))
    print(s(4))
    print(s(5))