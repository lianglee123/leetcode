
# class Solution {
# public List<Integer> inorderTraversal(TreeNode root) {
# List<Integer> list = new ArrayList<Integer>();
#
# Stack<TreeNode> stack = new Stack<TreeNode>();
# TreeNode cur = root;
#
# while(cur!=null || !stack.empty()){
# while(cur!=null){
# stack.add(cur);
# cur = cur.left;
# }
# cur = stack.pop();
# list.add(cur.val);
# cur = cur.right;
# }
#
# return list;
# }
#
# }


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        cur = root
        res = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res


class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                if node.right is not None:
                    stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                if node.left is not None:
                    stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res


if __name__ == '__main__':
    from utils import serialize, deserialize, drawtree
    tree = deserialize("[[1,null,2,3]]")
    # drawtree(tree)
    s = Solution2().inorderTraversal
    print(s(tree))
