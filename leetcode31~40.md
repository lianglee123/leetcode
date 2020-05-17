### 31. Next Permutation

#### Round1

这个题要通过观察法做。

https://www.cnblogs.com/grandyang/p/4428207.html

https://leetcode.com/problems/next-permutation/

做之前现在一道InPlace Reverse arrary的题。

#### Round2
过程：
1. 从右往左找到第一个变小的数，其位置记为x. 要注意到一个隐藏的信息：此时x后面的数都是按逆序(从大到小)排序的
2. 从右往左找到第一个大于等于nums[x]的数，其位置记为y。交换nums[x] 和 nums[y] in place.
此时x后面的数依然是按照逆序排列的。
3. reverse x后面的数，使其按照正序排列。
4. 如果找不到x, 就直接reverse整个数组，即可得到最小的数。
------

### 32. Longest Valid Parentheses

#### Round1

https://baihuqian.github.io/2018-06-02-longest-valid-parentheses/

**方法一**: dp, dp[i]表示以i结尾的最长合法串
那么：
dp[0] = 0
    - 如果s[i]=='(', dp[i] = dp[i-1]
    - 如果s[i]==')'
        - 如果s[i-1]=='(', dp[i] = 2 + dp[i-2]
        - 如果s[i-1]==')', a=dp[i-1], j=i-a
            - 如果s[j]的值为'(', dp[i]=dp[i-1]+2+dp[j-1]
            - 如果s[j]的值是')', dp[i]=dp[i-1]
方法二：使用栈

---

### 33. Search in Rotated Sorted Array

#### Round1
先用二分法找到分割点，然后使用二分法查找
要注意这道题的条件是Array里没有重复的值，否则就难办了。

---

### 34. Find First and Last Position of Element in Sorted Array

#### Round1

法1：先找到这个值，然后向左右扩展。但最差的情况会有O(n)的复杂度。

法2: 完全二分法？
也是非常简单的，问题关键在于，low, 和high的移动方法
做这个题之前，应该先做一道单纯的binarySearch的题

---

### 35. Search Insert Position

#### Round1

二分法

#### Round2

简单的题，我也总是做错。

s指针的含义：s左边的数都小于target(不包括s)

e指针的含义，e右边的数都大于target(不包括e)

所以最终返回s就好了。

终止条件为s<=e,

---

### 36. Valid Sudoku

#### Round1

我能想到只是暴力了。

但是如何方便的查询没有重复的？使用Set



[好好规划，可以只迭代一遍, 同时迭代行和列，秒呀](https://leetcode.com/problems/valid-sudoku/discuss/15450/Shared-my-concise-Java-code)



[用位操作判断是否重复，更加快速](https://leetcode.com/problems/valid-sudoku/discuss/15452/C%2B%2B-very-simple-and-easy-understand.-using-bit-operation)


---

### 37. Sudoku Solver

#### Round 1

这题我以前做过，但是以前事用暴力法做的。

[一个回溯法](https://leetcode.com/problems/sudoku-solver/discuss/15752/Straight-Forward-Java-Solution-Using-Backtracking)

回溯是不是重试？回溯，回退


繁殖算法是什么？

2MS的算法：https://leetcode.com/problems/sudoku-solver/discuss/15748/Sharing-my-2ms-C%2B%2B-solution-with-comments-and-explanations.

---

### 38. Count and Say

#### Round1

https://www.cnblogs.com/TenosDoIt/p/3776356.html

---

### 39. Combination Sum

#### Round1

**法一：**回溯法：牛逼的回溯法。完全掌握这个博主的这篇文章

https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)

**法二：**DP

**法三：**dfs

---

### 40. Combination Sum II

#### Round1

同39，只不过考虑处理重复的问题

