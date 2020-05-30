from typing import List


class Solution:
    """
    Time Limit Exceeded Answer
    """
    def isMatch(self, s: str, p: str) -> bool:
        print("isMatch: ", s, p)
        if not p:
            return not s
        if p[0] == '?':
            if len(s) > 0:
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        elif p[0] == '*':
            for i in range(len(s)+1):
                print("---> i: ", i, s[i:], p[1:])
                if self.isMatch(s[i:], p[1:]):
                    return True
        else:
            if len(s) > 0:
                return p[0] == s[0] and self.isMatch(s[1:], p[1:])
            else:
                return False


class Solution2:
    """
    Time Limit Exceeded Answer
    """

    def isMatch(self, s: str, p: str) -> bool:
        return self._isMatch([i for i in s], [i for i in p])

    def _isMatch(self, s: List[str], p: List[str]) -> bool:
        if not p:
            return not s
        if p[0] == '?':
            if len(s) > 0:
                return self._isMatch(s[1:], p[1:])
            else:
                return False
        elif p[0] == '*':
            for i in range(len(s)+1):
                if self._isMatch(s[i:], p[1:]):
                    return True
        else:
            if len(s) > 0:
                return p[0] == s[0] and self._isMatch(s[1:], p[1:])
            else:
                return False


class SolutionFiniteStateMachine:
    """
    不理解的答案
    """
    def isMatch(self, s, p):
        transfer = {}
        state = 0
        for char in p:
            if char == '*':
                transfer[(state, char)] = state
            else:
                transfer[(state, char)] = state + 1
                state += 1
        accept = state
        states = set(0)
        for char in s:
            _states = set()
            for token in [char, '*', '?']:
                for at in states:
                    next_state = transfer.get((at, token))
                    if next_state is not None:
                        _states.add(next_state)
            states = _states
        return accept in state

if __name__ == '__main__':
    s = Solution2().isMatch
    # assert s("aa", "a") == False
    # assert s("aa", "*") == True
    # assert s("adceb", "*a*b") == True
    # assert s("acdcb", "a*c?b") == False
    # assert s("", "*") == True
    assert s("aa", "*") == True