### 21. Merge Two Sorted Lists

#### Round1

通用做法，迭代归并。

---

### 22. Generate Parentheses

#### Round1

题目的Topic是BackTrace， 但我真不知道BackTracing的含义。

但这道题我徒手做出来了。

依然要好好探索一下BackTrace的含义

---

### 23. Merge k Sorted Lists

#### Round1

简单的做法两两合并，但是复杂度

设M个List, 每个List中N个元素。

简单的按照顺序逐个合并，复杂度为（2+3+4+...+M)*N, 为M**2*N

如果递归的两两合并，复杂度为MN*lgM

即使又线性方法，每个元素迭代一遍也要MN次，所以MNlgM是可以接受的。

另外还有借助其他数据结构的方法，但我还不知道，需要研究。

---

### 24. Swap Nodes in Pairs

#### Round1

链表操作，不涉及任何算法思想，只涉及到骚操作。

如何把一整个链表的Swap的操作，变成可迭代的一步步小操作？计算机就是适合这种事。

先在纸上一小步一小步的画出来，找出操作规律，然后再写代码。

*我的实现方法太低效了*

要同时用递归的和非递归的方法完成

---

### 25. Reverse Nodes in K Group（hard)

#### Round1

这个题和24题一脉相承。

---

### 26. Remove Duplicates from Sorted Array

#### Round1

双指针，交换。

---

### 27. Remove Element

双指针，交换。

通过26和27可以学会数组的InPlace 操作法，快排也用得到。

---

### 28. Implement strStr()

#### Round1

粗暴的做法就是二次迭代。

非粗暴的做法可能需要使用到和KMP相关的东西。

必须理解KMP

---

### 29. Divide Two Integers

#### Round1

位运算这种题都适合用Java或C写。

位运算

把Dividend拆解为

Dividend = Dividor * 2^m + Dividor *2^n + ... + Dividor + y

---

### 30. Substring with Concatenation of All Words（Hard）

#### Round1

我能想到的知识暴力解法了

暴力求解但是要注意使用每个Word长度都相同这个条件。
发现一种不用compare_map的方法，牛逼！(https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13658/Easy-Two-Map-Solution-(C%2B%2BJava))

