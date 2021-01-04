class SolutionBFS:
    """
    O(N)的复杂度
    https://leetcode.com/problems/jump-game-ii/discuss/18028/O(n)-BFS-solution
    """
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        level = 0
        cur_max = 0   # 当前Level的能达到的最远位置
        next_max = 0  # 下一个Level能达到的最远位置(next Level的上界)
        i = 0     # 如何求next_max呢？只要迭代这个Level的所有元素，找到下一步所能到达的最远位置即可。
        while i<= cur_max:
            while i <= cur_max: # 这个循环的目的是迭代当前Level, 找到next_max。
                next_max = max(next_max, nums[i]+i)
                if next_max >= (len(nums) - 1):
                    return level+1
                i += 1

            level += 1  # 进入下一层
            cur_max = next_max  # cur_max记录当前所能到达的最远距离。
        return -1

class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        l = len(nums)

        cur_max = 0
        next_max = 0
        jump = 0
        for i in range(l):
            next_max = max(nums[i]+i, next_max)
            if next_max >= l-1:
                return jump + 1
            if i == cur_max:  # 进入下一层
                print("enter next level: ", i, cur_max, next_max, "jump: ", jump, '-->', jump+1)
                cur_max = next_max
                jump += 1
        return jump




if __name__ == '__main__':
    s = Solution().jump
    # nums = [2,3,1,1,4]
    nums = [2,3,1,4,4]
    print(s(nums))