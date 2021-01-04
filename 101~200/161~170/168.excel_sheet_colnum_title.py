class Solution:
    def convertToTitle(self, n: int) -> str:
        if n == 0:
            return ""
        else:
            n, rem = divmod((n-1), 26)
            return self.convertToTitle(n) + chr(rem + ord('A'))


