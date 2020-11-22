from typing import *



class Solution:
    """
    https://leetcode.com/problems/integer-to-english-words/discuss?currentPage=1&orderBy=most_posts&query=
    """
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n/10-2]] + words(n%10)
            if n < 1000:
                return [to19[n/100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return words(n/1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'


class Solution2:
    """
    https://leetcode.com/problems/integer-to-english-words/discuss?currentPage=1&orderBy=most_posts&query=
    """
    to19 = ' One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = ' Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

    thousands = ("", "Thousand", "Million", "Billion")

    def numberToWords(self, num):
        if num == 0: return "Zero"

        i = 0
        words = ""
        while num > 0:
            if num % 1000 != 0:
                words = self.helper(num % 1000) + " " + Solution2.thousands[i] + " " + words
            num //= 1000
            i += 1
        return words.strip()

    def helper(self, num):
        """转化三位数"""
        if num == 0:
            return ""
        elif num < 20:
            return Solution2.to19[num]
        elif num < 100:
            return Solution2.tens[num/10] + " " + self.helper(num % 10)
        else:
            return Solution2.to19[num / 100] + " Hundred " + self.helper(num % 100)



if __name__ == '__main__':
    s = Solution2().numberToWords
    print(s(1000))