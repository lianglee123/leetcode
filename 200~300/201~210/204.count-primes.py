



class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        recorders = [True]*(n+1)
        count = 0
        for i in range(2, n):
            if recorders[i] is False:
                continue
            tmp = i
            count += 1
            while tmp + i <= n:
                newTmp = tmp + i
                recorders[newTmp] = False
                tmp = newTmp

        return count


if __name__ == '__main__':
    s = Solution().countPrimes
    print(s(10)==4)
    print(s(2))
    print(s(3))
    print(s(4))
    print(s(5))


