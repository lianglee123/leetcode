class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_token = path.split("/")

        for t in path_token:
            if t == '..' and stack:
                stack.pop()
            else:
                if t not in ('..', '.', ""):
                    stack.append(t)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    s = Solution().simplifyPath
    p1 = "/home/"
    p2 = "/../"
    p3 = "/"
    p4 = "/./"
    p5 = "/home//foo"
    p6 = "/a/./b/../../c/"
    print(p1 + '-->', s(p1))
    print(p2 + '-->', s(p2))
    print(p3 + '-->', s(p3))
    print(p4 + '-->', s(p4))
    print(p5 + '-->', s(p5))
    print(p6 + '-->', s(p6))