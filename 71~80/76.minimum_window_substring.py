class Solution:
    """
    subString的题，有一种通用做法：双指针 + hashMap
    双指针可以都是从头开始迭代的，类似解法的模板
    https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
    """
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        minLeft = 0
        minRight = 0
        minLen = len(s)
        foundFlag = False

        need_map = {}  # 需求map, 当里面所有的值都小于等于0时，说明需求被满足了。
        for c in t:
            need_map[c] = need_map.get(c, 0) + 1
        # 使用count判断是否所有的字符的需求都被满足了，棒
        # count其实是一个need_map的标志位，用来表示是否need_map的所有值都被满足了。
        # count可以被如下语句替代：all(need <= 0 for need in need_map.values())
        count = len(t)


        i = 0
        j = 0
        while j < len(s):
            c = s[j]
            if c in need_map:
                need_map[c] -= 1
                if need_map[c] >= 0:  # c是一个有效字符
                    count -= 1

            # 找到了目标字串，此时count == 0, t_map的所有值要么为0，要么为负数
            # 进入这个循环，智能说明i与j之间出现和合法的字串，但是不一定是最小的，因为i可能还能收缩
            while count == 0:  # 为什么要加i<=j的条件，难道i能大于j吗
                foundFlag = True
                curLen = j - i + 1
                if curLen <= minLen:
                    minLeft = i
                    minRight = j
                    minLen = curLen

                # shrink left
                leftC = s[i]
                if leftC in need_map:  # leftC在t_map的情况下，什么情况才能收缩呢？
                    need_map[leftC] += 1
                    if need_map[leftC] > 0:  # 一旦need_map中有一个值大于0，说明又有字符需要满足了
                        count += 1
                i += 1

            j += 1

        return s[minLeft:minRight+1] if foundFlag else ''
