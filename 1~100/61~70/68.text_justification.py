

class Solution:
    """
    https://leetcode.com/problems/text-justification/discuss/24902/Java-easy-to-understand-broken-into-several-functions
    """
    def fullJustify(self, words, maxWidth):
        left = 0
        result = []
        while left < len(words):
            right = self.findRight(left, words, maxWidth)
            result.append(self.justify(left, right, words, maxWidth))
            left = right + 1
        return result

    def findRight(self, left, words, maxWidth):
        right = left
        sum = len(words[right])
        right += 1
        while right < len(words) and (sum + 1 + len(words[right])) <= maxWidth:
            sum += (1 + len(words[right]))
            right += 1
        return right - 1

    def justify(self, left, right, words, maxWidth):
        if right == left:
            return words[left].ljust(maxWidth)
        numSpaces = right - left
        totalSpaces = maxWidth - sum(len(words[i])for i in range(left, right+1))

        isLastLine = right == (len(words) - 1)
        space = " " if isLastLine else " " * (totalSpaces//numSpaces)
        remainder = 0 if isLastLine else totalSpaces % numSpaces
        res = ''
        for i in range(left, right+1):
            res += words[i]
            res += space
            if remainder > 0:
                res += " "
                remainder -= 1
        return res.strip().ljust(maxWidth)


class Solution2:
    """
    https://leetcode.com/problems/text-justification/discuss/24891/Concise-python-solution-10-lines.
    """
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]


if __name__ == '__main__':
    s = Solution().fullJustify
    text = """It was the best of times, it was the worst of times,
it was the age of wisdom, it was the age of foolishness,
it was the epoch of belief, it was the epoch of incredulity,
it was the season of Light, it was the season of Darkness,
it was the spring of hope, it was the winter of despair,
we had everything before us, we had nothing before us,
we were all going direct to Heaven, we were all going direct
the other way--in short, the period was so far like the present
period, that some of its noisiest authorities insisted on its
being received, for good or for evil, in the superlative degree
of comparison only."""
    words = text.split()
    for w in s(words, 35):
        print(w)
