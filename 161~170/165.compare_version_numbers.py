
def cmp(a, b):
    return (a > b) - (a < b)

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = (list(map(int, v.split('.'))) for v in (version1, version2))
        d = len(v2) - len(v1)
        return cmp(v1 + [0]*d, v2 + [0]*-d)


if __name__ == '__main__':
    s = Solution().compareVersion
    print(s("0.1", "1.1"))
    print(s("1.0.1", "1"))
    print(s("7.5.2.4", "7.5.3"))
    print(s("1.01", "1.001"))
    print(s("1.0", "1.0.0"))
