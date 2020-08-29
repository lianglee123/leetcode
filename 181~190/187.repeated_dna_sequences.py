class Solution:
    L = 10
    HIGHT_WEIGHT = (4 ** (L-1))

    def findRepeatedDnaSequences(self, s):
        n = len(s)
        if n <= self.L:
            return []
        values = list(map(self.toInt, s))
        # print(values)
        result = set()
        seen = set()
        currHash = self.hash(values[:self.L])
        seen.add(currHash)

        for i in range(self.L, len(values)):
            currHash = self.increHash(currHash, values[i])
            # print("i: ", i, values[i], s[i+1-self.L:i+1], values[i+1-self.L:i+1], currHash)
            if currHash in seen:
                # print("not found")
                result.add(s[i+1-self.L:i+1])
            else:
                seen.add(currHash)
            # print("seen:", seen)
        return list(result)

    def hash(self, values):
        res = 0
        for i in range(len(values)):
            old = res
            res =  res*4 + values[i]
            # print(old, values[i], res)
        # print("hashValues: ", values, "hash: ", res)
        return res

    def increHash(self, oldHash, v):
        # if (oldHash == 5):
            # print("hashCalc: ", oldHash, self.HIGHT_WEIGHT, oldHash%self.HIGHT_WEIGHT, v)
        return (oldHash % self.HIGHT_WEIGHT) * 4 + v

    def toInt(self, c):
        if c == 'A':
            return 0
        elif c == 'C':
            return 1
        elif c == 'G':
            return 2
        elif c == 'T':
            return 3
        else:
            raise ValueError("c is inValid")

if __name__ == '__main__':
    s = Solution().findRepeatedDnaSequences
    param = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(s(param))
    print("#"*10)
    # s2 = Solution()
    # print(s2.hash([0, 0, 0, 0, 0, 1, 1, 1, 1, 1]))