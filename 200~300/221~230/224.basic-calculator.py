from typing import *




def strToInt(s):
    n = 0
    for c in s:
        n = 10*n + (ord(c)-ord('0'))
    return n

"""
计算器的进化
https://leetcode-cn.com/problems/basic-calculator/solution/chai-jie-fu-za-wen-ti-shi-xian-yi-ge-wan-zheng-j-2/
"""
class Solution_1:
    """
    只有加减法, 且字符种没有空格
    """
    def calculate(self, s):
        stack = []
        num = 0
        sign = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = 10 * num + (ord(c) - ord('0'))
            if (not c.isdigit()) or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                sign = c
                num = 0
        return sum(stack)

class Solution_2:
    """
    只有加减法, 字符中有了空格
    """
    def calculate(self, s):
        stack = []
        num = 0
        sign = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = 10 * num + (ord(c) - ord('0'))
            if (not c.isdigit() and c != " ") or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                sign = c
                num = 0
        return sum(stack)


class Solution_3:
    """
    加减法 + 空格 +  乘除
    """
    def calculate(self, s):
        stack = []
        num = 0
        sign = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = 10 * num + (ord(c) - ord('0'))
            if (not c.isdigit() and c != " ") or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    pre = stack.pop()
                    stack.append(pre * num)
                elif sign == '/':
                    pre = stack.pop()
                    stack.append(pre/num)
                sign = c
                num = 0
        return sum(stack)


class Solution_3Ptr5:
    """
    加减法 + 空格 +  乘除
    改成使用pop消费字符，而不是使用ptr，为下一步递归消费做准备，
    因为使用stk的pop消费，代码的调用栈的上下层可以共享消费进度，如果使用指针就不太能行。
    """
    def calculate(self, s):
        return self.helper(list(s))

    def helper(self, s: List):
        stack = []
        num = 0
        sign = '+'
        while s:
            c = s.pop()
            if c.isdigit():
                num = 10 * num + (ord(c) - ord('0'))
            if (not c.isdigit() and c != " ") or not s:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    pre = stack.pop()
                    stack.append(pre * num)
                elif sign == '/':
                    pre = stack.pop()
                    stack.append(pre/num)
                sign = c
                num = 0
        return sum(stack)


class Solution_4:
    """
    加减法 + 空格 +  乘除 + 括号
    当碰到括号的时候，递归执行
    """
    def calculate(self, s):
        return self.helper(list(s))

    def helper(self, s: List):
        stack = []
        num = 0
        sign = '+'
        while s:
            c = s.pop(0)
            if c.isdigit():
                num = 10 * num + (ord(c) - ord('0'))
            if c == '(':
                num = self.helper(s)
            if (not c.isdigit() and c != " ") or not s:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    pre = stack.pop()
                    stack.append(pre * num)
                elif sign == '/':
                    pre = stack.pop()
                    stack.append(pre/num)
                sign = c
                num = 0
            if c == ')':
                break
        return sum(stack)

class Solution:
    """
    加减法 + 空格 +  乘除 + 括号
    当碰到括号的时候，递归执行
    但是这个答案超出时间限制了
    """
    def calculate(self, s):

        return self.helper(list(reversed(s)))

    def helper(self, s: List):
        stack = []
        num = 0
        sign = '+'
        while s:
            c = s.pop()
            if c.isdigit():
                num = 10 * num + (ord(c) - ord('0'))
            if c == '(':
                num = self.helper(s)
            if (not c.isdigit() and c != " ") or not s:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                sign = c
                num = 0
            if c == ')':
                break
        return sum(stack)


class Solution2:
    """
    作者：LeetCode
链接：https://leetcode-cn.com/problems/basic-calculator/solution/ji-ben-ji-suan-qi-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    这种解法的栈是用来保存当碰到括号时的符号和值
    这种解法耗时0.06s, 而Solution_4耗时6s, 相差100倍，而且两个都是o(N)的复杂度, 注要是因为s.pop(0)的复杂度是o(n^2)
    """
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative
        for ch in s:
            if ch.isdigit():
                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)
            elif ch == '+':
                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand
                # Save the recently encountered '+' sign
                sign = 1
                # Reset operand
                operand = 0
            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == '(':
                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)
                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0
            elif ch == ')':
                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand
                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign
                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand
                # Reset the operand
                operand = 0
        return res + sign * operand

if __name__ == '__main__':
    import time
    s = Solution_3().calculate
    print(s('1*2'))
    print(s(' 1 + 2  + 3'))
    print(s('1+2+(3-1)-(5-2)'))
