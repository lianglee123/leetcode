

def my_assert(val, expect):
    if val == expect:
        return
    else:
        err = "%s not equal %s" % (val, expect)
        raise AssertionError(err)


class Solution:
    """
    这道题的关键在于要搞懂left_ptr行进的方向。
    一开始我使用的错误的更新left_ptr的方法 if char in index_map: left_ptr = index_map[char] + 1 （特例：abba)
    另外一种正确的做法是：if (char in index_map) and (index_map[char] >= left_ptr): left_ptr = index_map[char] + 1 (
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}
        res = 0
        left_ptr = 0
        right_ptr = 0
        while right_ptr < len(s):
            char = s[right_ptr]
            # if char in index_map:
            #     left_ptr = max(index_map[char] + 1, left_ptr)
            if (char in index_map) and (index_map[char] >= left_ptr):
                left_ptr = index_map[char] + 1
            index_map[char] = right_ptr
            right_ptr += 1
            res = max(res, right_ptr - left_ptr)
        return res


if __name__ == '__main__':
    s = Solution().lengthOfLongestSubstring
    my_assert(s("abcabcbb"), 3)
    my_assert(s("bbbb"), 1)
    my_assert(s("abba"), 2)
    my_assert(s("pwwkew"), 3)
    my_assert(s("abbbb"), 2)
    my_assert(s("abcabcbb"), 3)
    my_assert(s("a"), 1)
    my_assert(s("dvdf"), 3)
