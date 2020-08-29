from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class WrongSolution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        return self.helper(A, B, 0)

    def helper(self, A: TreeNode, B: TreeNode, level) -> bool:
        if not B:
            return True
        if not A:
            return False
        print("#"*30)
        print(level*2*"#",A)
        print(level*2*"#",B)
        if A.val == B.val and self.helper(A.left, B.left, level+1) and self.helper(A.right, B.right, level+1):
            print(level*2*"#", "val==val", True)
            return True
        elif self.helper(A.left, B, level+1):
            print(level*2*"#", "A.left, B", True)
            return True
        elif self.helper(A.right, B, level+1):
            print(level*2*"#", "A.right, B", True)
            return True
        else:
            print(level*2*"#", False)
            return False



        # print(level*2*"#", A.val == B.val and self.helper(A.left, B.left, level+1) and self.helper(A.right, B.right, level+1))
        # print(level*2*"#", self.helper(A.left, B, level+1))
        # print(level*2*"#", self.helper(A.right, B, level+1))
        # return (A.val == B.val and self.helper(A.left, B.left, level+1) and self.helper(A.right, B.right)) or \
        #        self.helper(A.left, B) or \
        #        self.helper(A.right, B)

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        return self.isSub(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def isSub(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.isSub(A.left, B.left) and self.isSub(A.right, B.right)


if __name__ == '__main__':
    from utils.tree_node_utils import deserialize, drawtree
    n1 = deserialize("[1,0,1,-4,-3]")
    # drawtree(n1)
    n2 = deserialize("[1,-4")
    s = Solution().isSubStructure
    print(s(n1, n2))
