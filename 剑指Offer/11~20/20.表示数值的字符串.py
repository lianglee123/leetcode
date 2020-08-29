from typing import *

import re


class Solution:
    p = re.compile(r'^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$')
    def isNumber(self, s: str) -> bool:
        return bool(self.p.match(s.strip()))


from enum import  Enum, unique


@unique
class State(Enum):
    INITIAL = 1
    INT_SIGN = 2
    INTEGER = 3
    POINT = 4
    POINT_WITHOUT_INT = 5
    FRACTION = 6
    EXP = 7
    EXP_SIGN = 8
    EXP_NUMBER = 9
    END = 10


class CharType(Enum):
    NUMBER = 1
    EXP = 2
    POINT = 3
    SIGN = 4
    SPACE = 5
    ILLEGAL = 6
    @staticmethod
    def toCharType(char: str):
        if char.isdigit():
            return CharType.NUMBER
        elif char.lower() == "e":
            return CharType.EXP
        elif char == ".":
            return CharType.POINT
        elif char == "+" or char == "-":
            return CharType.SIGN
        elif char == " ":
            return CharType.SPACE
        else:
            return CharType.ILLEGAL



class Solution2:
    transfer = {
        State.INITIAL: {
            CharType.SPACE: State.INITIAL,
            CharType.NUMBER: State.INTEGER,
            CharType.POINT: State.POINT_WITHOUT_INT,
            CharType.SIGN: State.INT_SIGN,

        },
        State.INT_SIGN: {
            CharType.NUMBER: State.INTEGER,
            CharType.POINT: State.POINT_WITHOUT_INT,
        },
        State.INTEGER: {
            CharType.NUMBER: State.INTEGER,
            CharType.EXP: State.EXP,
            CharType.POINT: State.POINT,
            CharType.SPACE: State.END,
        },
        State.POINT: {
            CharType.EXP: State.EXP,
            CharType.SPACE: State.END,
            CharType.NUMBER: State.FRACTION,
        },
        State.FRACTION: {
            CharType.NUMBER: State.FRACTION,
            CharType.EXP: State.EXP,
            CharType.SPACE: State.END,
        },
        State.POINT_WITHOUT_INT: {
            CharType.NUMBER: State.FRACTION
        },
        State.EXP: {
            CharType.SIGN: State.EXP_SIGN,
            CharType.NUMBER: State.EXP_NUMBER,
        },
        State.EXP_SIGN: {
            CharType.NUMBER: State.EXP_NUMBER,
        },
        State.EXP_NUMBER: {
            CharType.NUMBER: State.EXP_NUMBER,
            CharType.SPACE: State.END,
        },
        State.END: {
            CharType.SPACE: State.END,
        }
    }
    validEndState = {
        State.INTEGER,
        State.POINT,
        State.FRACTION,
        State.EXP_NUMBER,
        State.END,
    }

    def isNumber(self, s: str) -> bool:
        st = State.INITIAL
        for ch in s:
            typ = CharType.toCharType(ch)
            if typ not in self.transfer[st]:
                return False
            st = self.transfer[st][typ]
        return st in self.validEndState


if __name__ == '__main__':
    from utils import assert_eq
    s = Solution2().isNumber
    assert_eq(s("123"), True)
    assert_eq(s("111"), True)
    assert_eq(s("000"), True)
    assert_eq(s(".000"), True)
    assert_eq(s("1.12"), True)
    assert_eq(s("+1.12"), True)
    assert_eq(s("-1.12"), True)
    assert_eq(s("-1.12e10"), True)
    assert_eq(s("  -1.12e10  "), True)