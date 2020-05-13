from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:  # 这里的边界条件为什么模板代码不用特殊处理？
            return []

        count_map = {}
        for w in words:
            if w in count_map:
                count_map[w] += 1
            else:
                count_map[w] = 1

        w_l = len(words[0]) if len(words) > 0 else 0
        target_l = w_l * len(words)

        i = 0
        res = []
        while (i + target_l) <= len(s):
            seen = {}
            j = i
            for _ in range(len(words)):
                word = s[j:j+w_l]
                if word in count_map:
                    if word in seen:
                        seen[word] += 1
                    else:
                        seen[word] = 1
                    if seen[word] > count_map[word]:
                        break
                else:
                    break
                j += w_l
            if j == i + target_l:   # 题解的关键在这里，这里不用对比两个Map
                res.append(i)
            i += 1
        return res

    def compare_map(self, map1, map2):
        if len(map1) != len(map2):
            return False
        for key, value in map1.items():
            if key not in map2 or map2[key] != value:
                return False
        return True


if __name__ == '__main__':
    s = Solution().findSubstring
    # r = s("wordgoodgoodgoodbestword",
    #   ["word","good","best","good"])
    # print(r)
    r = s("asdf", [])
    print(r)