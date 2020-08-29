class Solution:
    def reverseWords(self, s: str) -> str:
        tokens = list(filter(lambda x: x, s.split()))
        tokens.reverse()
        return " ".join(tokens)


if __name__ == '__main__':
    s = Solution().reverseWords
    print(s("the sky is bule"))
    print(s("  hello world!  "))
    print(s("a good   example"))