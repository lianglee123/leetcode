from typing import *


class Solution:
    """
    https://baihuqian.github.io/2018-07-28-encode-and-decode-strings/
    关于此题的思考，是，两部分。
    第一部分：在编码时，需要使用原字符串数组中没有的字符串，把字符串数组连接起来。
    但是如果原字符串中已经有分隔符了，那该怎么办。通过转义把这些字符转义，注意这个转义字符必须是可逆的。
    第二部分：那么如何搞出一个可逆的转义方法呢？
    转义的第一步是把原有字符串替换为相应的转义字符串。反转义时再替换出来。
    转义: s.replace(A, B)
    反转义：s.replace(B, A)
    转义反转义时有一个问题，会把s中原有的B也变为A，这是不被允许的。所以要保证
    再转义时，把s中原有的B也给转换掉。有没有可能一步s.replace(A, B)就能达到这个目的？
    有，那就是让B包含A, 这样如果s中原有的B就会也会被转换。
    单纯的转义算法有许多，但是，最简答的转义算法当然是用replace, 不过这里的replace还有一个约束
    是转义后不能出现第一步选定的分隔符。
    1. 选定分隔符。%
    2. 转义算法：
        1. 转义后的字符不能出现第一步出现的分隔符。（继B不能包含分隔符）
        2. 转义算法自身的要求：转移后可以正常转义回来。如果使用replace作为转义算法，就要求s.replace(%,B)
            B一定要包含%，但是如果B包含%了就无法满足分隔符的要求，所以可以调整分隔符为%%

    那么，像python，go,这些语言里是如何实现转义的呢？注：这些编程语言的转义算法是不考虑分隔符的限制的。
    python的转义字符是使用“\”放到特殊字符的前面，这些特殊字符是用键盘难以直接输入的。那么当需要表示“\”，
    就也需要用转义字符来处理了。
    格式化字符“%”和转义字符类似。
    """
    def encode(self, strs):
        if not strs:
            return ""
        return "//".join([s.replace("/", "#/#") for s in strs]) + "//"

    def decode(self, s):
        if len(s) == 0:
            return []
        return [seg.replace("#/#", "/") for seg in s.split("//")][:-1]



class Solution2:
    """这个方案把每个字符串的长度写在字符头使用 '长度 + / + 字符串'"""
    def encode(self, strs):
        pass

    def decode(self, s):
        pass


class Solution3:
    """
    这个方案就使用json的序列化方案
    但这种我现在还不会
    """
    def encode(self, strs):
        pass

    def decode(self, s):
        pass
