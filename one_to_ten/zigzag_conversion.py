class Solution:
    def convert(self, s: str, numRows: int) -> str:
        char_list = [c for c in s]
        res = [[]for i in range(numRows)]

        l = len(s)
        i = 0
        while i < l:
            idx = 0
            while idx < numRows and i < l:
                res[idx].append(char_list[i])
                i += 1
                idx += 1

            idx = numRows - 2
            while idx >= 1 and i < l:
                res[idx].append(char_list[i])
                i += 1
                idx -= 1

        res = [''.join(i)for i in res]
        return ''.join(res)
