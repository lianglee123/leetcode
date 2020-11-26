from typing import *


class Solution:
    """
    https://www.cnblogs.com/grandyang/p/5226206.html
    博弈的问题，竟然能用这种方式。那么292题也能用这种方式了
    """
    def canWin(self, s):
        for i in range(1, len(s)):
            if s[i] == "+" and s[i-1] == "+" and not self.canWin(s[0:i-1] + '--' + s[i+1:]):
                return True
        return False


