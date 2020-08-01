class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            print(start, end)
            while (not self.valid_char(s[start])) and start < end:
                start += 1
            while (not self.valid_char(s[end])) and end > start:
                end -= 1
            if not self.equal(s[start], s[end]):
                return False
            start += 1
            end -= 1
        return True

    def valid_char(self, c):
        return ("9">=c>="0") or ("A"<=c<= "Z") or ("z">=c>= "a")

    def equal(self, c1, c2):
        return c1 == c2 or (self.isAlpha(c1) and self.isAlpha(c2) and abs(ord(c1) - ord(c2))==32)

    def isAlpha(self, c):
        return "A"<=c<="Z" or "a"<=c<="z"


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, da canal: Panama"))
    print(s.isPalindrome("race a car"))
