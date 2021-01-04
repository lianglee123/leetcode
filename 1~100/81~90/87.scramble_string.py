class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        if not self.same_letters(s1, s2):
            return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[0:i], s2[-i:]) and self.isScramble(s1[i:], s2[0:-i]):
                return True
        return False

    def same_letters(self, s1, s2):
        letters = {}
        for i in range(len(s1)):
            letters[s1[i]] = letters.get(s1[i], 0) + 1
            letters[s2[i]] = letters.get(s2[i], 0) - 1
        return not any(letters.values())


if __name__ == '__main__':
    s = Solution()
    print(s.isScramble("great", "rgtae"))

    # print(s.same_letters("great", "rgtae"))
    # print(s.same_letters("aaaa", "aaab"))