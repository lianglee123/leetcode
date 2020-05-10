class Solution(object):
    def isValid(self, s: str) -> bool:
        if (len(s) % 2 != 0):
            return False
        stack = []
        for i in s:
            if i in ('(', '[', '{'):
                stack.append(i)
            elif i in (')', ']', '}'):
                if len(stack) == 0:
                    return False
                c = stack.pop()
                if i == ')' and c != '(':
                    return False
                elif i == ']' and c != '[':
                    return False
                elif i == '}' and c != '{':
                    return False
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution().isValid
    print(s('()[]{}'))