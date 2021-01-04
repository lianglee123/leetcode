from  typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        self.res = []
        self.dfs(s, len(s)-1, [])
        return self.res

    def dfs(self, remainder, end, temp):
        if len(temp) == 4:
            if not remainder:
                self.res.append('.'.join(temp))
            return
        if len(remainder) >= 1:
            temp.append(remainder[:1])
            self.dfs(remainder[1:], end, temp)
            temp.pop()

        if len(remainder) >= 2 and  not remainder[:2].startswith('0'):
            temp.append(remainder[:2])
            self.dfs( remainder[2:], end, temp)
            temp.pop()

        if len(remainder) >= 3 and remainder[:3] <= '255' and not remainder[:3].startswith('0'):
                temp.append(remainder[:3])
                self.dfs(remainder[3:], end, temp)
                temp.pop()


class Solution2:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    if 0 < len(s) - (i + j + k) <= 3:
                        a = s[:i]
                        b = s[i:i+j]
                        c = s[i+j:i+j+k]
                        d = s[i+j+k:]
                        if all(map(self.valid, [a, b, c, d])):
                            res.append('.'.join([a, b, c, d]))
        return res

    def valid(self, s):
        if len(s) == 1:
            return True
        elif len(s) == 2:
            return not s.startswith('0')
        elif len(s) == 3:
            return s <= '255' and not s.startswith('0')
        else:
            return False

# class Solution:
#     def restoreIpAddresses(self, s: str) -> List[str]:
#         self.res = []
#         self.dfs(s, 0, len(s)-1, [])
#         return self.res
#
#     def dfs(self, remainder, end, temp):
#         if not remainder:
#             return
#         print(pos)
#         i = pos
#         while i <= end:
#             temp.append(s[i:i+1])
#             self.dfs(s, pos+1, end, temp)
#             temp.pop()
#
#             if i+1 <= end:
#                 temp.append(s[i:i+2])
#                 self.dfs(s, pos+2, end, temp)
#                 temp.pop()
#
#             if i+2 <= end:
#                 temp.append(s[i:i+3])
#                 self.dfs(s, pos+3, end, temp)
#                 temp.pop()
#
#             i += 1


if __name__ == '__main__':
    s = Solution2().restoreIpAddresses
    print(s("25525511135"))
    print(s("1111"))
    print(s("0000"))
    print(s("010010"))
