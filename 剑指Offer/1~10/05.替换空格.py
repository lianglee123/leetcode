"""
该题再简单不过，可以用库函数，也可以遍历字符串，重新build一个字符串。
"""

class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")