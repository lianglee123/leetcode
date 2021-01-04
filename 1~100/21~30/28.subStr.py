from typing import *


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def KMP(s, p):
            """
            s为主串
            p为模式串
            如果t里有p，返回打头下标
            """
            nex = getNext(p)
            i = 0
            j = 0   # 分别是s和p的指针
            while i < len(s) and j < len(p):
                print(j)
                if j == -1 or s[i] == p[j]: # j==-1是由于j=next[j]产生
                    i += 1
                    j += 1
                else:
                    j = nex[j]

            if j == len(p): # j走到了末尾，说明匹配到了
                return i - j
            else:
                return -1

        def getNext(p):
            """
            p为模式串
            返回next数组，即部分匹配表
            """
            nex = [0] * (len(p) + 1)
            nex[0] = -1
            i = 0
            j = -1
            while i < len(p):
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    nex[i] = j     # 这是最大的不同：记录next[i]
                else:
                    j = nex[j]

            return nex

        return KMP(haystack, needle)


def prefixTable(needle: str):
    """
    next[i] 表示，needle[0:i](包括i)的最大相同真前缀真后缀的长度
    :param needle:
    :return:
    """
    if not needle:
        return []
    next = [0] * len(needle)
    j, i = 0, 1
    while i < len(needle):
        if needle[i] == needle[j]:
            next[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                next[i] = 0
                i += 1
            else:
                if j > 0:
                    j = next[j-1]
                else:
                    j = 0
    return next


def kmpSearch(haystack, needle):
    if not needle:
        return 0
    prefixT =  (needle)
    i, j = 0, 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                return i - len(needle)
        else:
            if j == 0:
                i += 1
            else:
                j = prefixT[j-1]
    return -1

def kmpSearchAll(haystack, needle):
    if not needle:
        return 0
    prefixT = prefixTable(needle)
    i, j = 0, 0
    res = []
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                res.append(i-len(needle))
                j = 0
        else:
            if j == 0:
                i += 1
            else:
                j = prefixT[j-1]
    return res



def broceSearch(haystack, needle):
    if not needle:
        return 0
    i, j = 0, 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                return i - len(needle)
        else:
            i = i - j + 1
            j = 0


def bruceSearchAll(haystack, needle):
    if not needle:
        return 0
    res = []
    i, j = 0, 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                res.append(i-len(needle))
                j = 0
        else:
            i = i - j + 1
            j = 0
    return res


def testSearchAll(fn):
    h = "abcabcabcabcabcabc"
    n = 'ab'
    res = fn(h, n)
    print(res)
    assert res == [0, 3, 6, 9, 12, 15]


def sundaySearch(haystack, needle):
    """
    i指针永远和pattern的头对齐，当i不匹配时，始终寻找最后一个字符串
    :param haystack:
    :param needle:
    :return:
    """
    if not needle:
        return 0
    nLen = len(needle)
    hLen = len(haystack)
    shiftTable = {}
    for i, c in enumerate(needle):
        shiftTable[c] = nLen - i
    i = 0
    while i <= hLen - nLen:
        j = 0
        while needle[j] == haystack[i+j]:
            j += 1
            if j >= nLen:
                return i
        else:
            c = haystack[i+len(needle)]
            offset = shiftTable[c] if c in shiftTable else nLen + 1
            i += offset
    return -1


def sundaySearchAll(haystack, needle):
    """
    i指针永远和pattern的头对齐，当i不匹配时，始终寻找最后一个字符串
    :param haystack:
    :param needle:
    :return:
    """
    if not needle:
        return 0
    nLen = len(needle)
    hLen = len(haystack)
    shiftTable = {}
    for i, c in enumerate(needle):
        shiftTable[c] = nLen - i
    i = 0
    res = []
    while i <= hLen - nLen:
        j = 0
        while needle[j] == haystack[i+j]:
            j += 1
            if j >= nLen:
                res.append(i)
                break
        c = haystack[i+len(needle)]
        offset = shiftTable[c] if c in shiftTable else nLen + 1
        i += offset
    return res



if __name__ == '__main__':
    # h = ''.join(['a', 'a', 'a', 'a', 'e', 'f', 'c', 'h', 'a', 'a', 'a', 'a', 'c', 'd'])
    # n = ''.join(['a', 'a', 'a', 'a', 'c', 'd'])
    # # s = Solution().strStr
    # # print("S: ", s(''.join(h), ''.join(n)))
    #
    print(prefixTable("aabaaf"))
    # i = kmpSearch(h, n)
    # assert h[i:len(n)+i] == n
    # print(broceSearch(h, n))
    testSearchAll(sundaySearchAll)