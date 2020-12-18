class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        result = [sign+str(n), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))
            print(stack, result, "n: ", n, "remainder: ", remainder)

        idx = stack.index(remainder)
        result.insert(idx+2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')


class Solution2:

    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return 0
        if denominator == 0:
            raise ValueError("denominator is zero")

        res = ""
        sign = "-" if numerator*denominator < 0 else ""
        res += sign

        num, den = abs(numerator), abs(denominator)
        n, rem = divmod(num, den)
        res += str(n)
        if rem == 0:
            return res
        res += "."
        recorder = {}
        while rem != 0:
            if rem in recorder:
                idx = recorder[rem]
                print(recorder, res)
                return res[0:idx] + "(" + res[idx:] + ")"
            else:
                recorder[rem] = len(res)
            print(recorder, res)
            n, rem = divmod(rem*10, den)
            res += str(n)
        return res


class Solution3:
    def fractionToDecimal(self, numerator, denominator):
        sign = '-' if numerator*denominator < 0 else ''
        n, rem = divmod(abs(numerator), abs(denominator))
        res = sign + str(n) + '.'
        recorder = {}
        while rem not in recorder:
            recorder[rem] = len(res)
            n, rem = divmod(rem*10, abs(denominator))
            res += str(n)
        idx = recorder[rem]
        res = res[0:idx] + "(" + res[idx:] + ")"
        return res.replace("(0)", "").rstrip(".")



if __name__ == '__main__':
    # s = Solution().fractionToDecimal
    # # print(s(10, 3))
    # print(s(29, 99))
    # print(s(100, 100))
    # print(s(100, 100))

    s2 = Solution2().fractionToDecimal
    # print(s2(29, 99))
    print(s2(100, 3))
    # print(s2(100, 100))
    # print(s2(1, 3))
    # print(s2(11, 100))
    # print(s2(1, 10000))
    # print(s2(0, 10000))

