from typing import List

class SolutionBackTrace:
    """
    public List<List<Integer>> permute(int[] nums) {
   List<List<Integer>> list = new ArrayList<>();
   // Arrays.sort(nums); // not necessary
   backtrack(list, new ArrayList<>(), nums);
   return list;
}

private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums){
   if(tempList.size() == nums.length){
      list.add(new ArrayList<>(tempList));
   } else{
      for(int i = 0; i < nums.length; i++){
         if(tempList.contains(nums[i])) continue; // element already exists, skip
         tempList.add(nums[i]);
         backtrack(list, tempList, nums);
         tempList.remove(tempList.size() - 1);
      }
   }
}

evolvement to solution below
    """
    pass

class SolutionBackTrace:
    def permute(self, nums):
        res = []
        used = [False]*len(nums)
        self.backTrack(res, nums, [], used)
        return res

    def backTrack(self, res, nums, temp_list, used):
        if len(temp_list) == nums:
            res.append([i for i in temp_list])
            return
        for i, n in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            temp_list.append(n)
            self.backTrack(res, nums, temp_list, used)
            del temp_list[-1]
            used[i] = False

class Solution:
    """
    backTrack
    https://leetcode.com/problems/permutations/discuss/18247/My-elegant-recursive-C%2B%2B-solution-with-inline-explanation
    """
    def permute(self, nums: List[int]):
        res = []
        self.backTrack(nums, 0, res)
        return res

    def backTrack(self, candidates, start, res):
        if start >= len(candidates):
            res.append([i for i in candidates])
            return
        for i in range(start, len(candidates)):
            candidates[start], candidates[i] = candidates[i], candidates[start]
            self.backTrack(candidates, start+1, res)
            candidates[start], candidates[i] = candidates[i], candidates[start]


if __name__ == '__main__':
    s = Solution().permute
    n = [1, 2, 3]
    for i in s(n):
        print(i)
