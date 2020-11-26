from typing import *

class Solution:
    """
    如果为4个石头，一定是先拿的输。
    所以如果是4的倍数，A拿n个，B就拿4-n个
    最终A还是会碰到4，
    如果不是四的倍数，AB的斩落地位交换
    """
    def canWinNim(self, n):
        return n % 4 != 0



class Solution2:
    """
    由294题触发的灵感, 虽然效率不太高
    """
    def canWinNim(self, n):
        if n == 0:
            return False
        elif n < 4:
            return True
        else:
            return not self.canWinNim(n-1) or \
                not self.canWinNim(n-2) or \
                not self.canWinNim(n-3)
