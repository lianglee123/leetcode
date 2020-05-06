

### 1. Two Sum



----

#### Round 1

解法：

只迭代一遍

使用一个Map, 记录每个value期待的对应值，一旦碰到该值，就停止。

#### [Round 2](./one_to_ten/two_sum.py)


---

### 2. Add Two Numbers

#### Round 1

这个简单，手动实现两数相加，但是要注意进位和溢出的问题。返回的值，仍然需要是链表。

溢出的问题如何解决？



---

### 3. Longest Substring Without Repeating Characters

#### Round1

Map + 双指针

最终结果为左右指针的最大差值。

左右指针都从最左侧开始，右指针迭代向前。

使用Map记录所有的遇到过的元素及其索引。

如果出现重复的，左指针就变动到原来元素的index上。

更新Map中重复元素的索引。

另外碰到到达尾部的无重复字符串，一定要及时停止。

---

### 4. Median of Two Sorted Arrays

#### Round 1

第一种方法是使用归并。这种算法复杂度是O(m+n), 过于简单不再说了。

如何找出一个O(long(M+N))的方法呢？

使用到了二分法的思想。

找中位数，可以转化为找第K大的数。

两个Sorted List的第K大的数，只有可能出现在这两个数组的前K位。

https://www.youtube.com/watch?v=LPFhl65R7ww

设两个数组的分别为X, Y

寻找前找到一个分割点，把两个数组分割为前

Xleft, Xright

Yleft, Yright

此时len(xLeft) + len(Left) == k

使用二分法寻找分割点，一旦分割点不合法，需要确定下一步的寻找方向(可通过判断不合法的的类型)。

此题要扩展为寻找前N个数的。最终的复杂度，会达到O(min(X, Y))

---

### 5. Longest Palindromic Substring

#### Round1

方法1. 找一个分割点，向两边扩展。https://leetcode.com/problems/longest-palindromic-substring/discuss/2928/Very-simple-clean-java-solution

方法2. 使用二维DP， dp[i,j]代表从s[i]~s[j]是否是回文数。

dp[i,j] = s[i]==s[j] && dp[i+1, j-1] (https://leetcode.com/problems/longest-palindromic-substring/discuss/2921/Share-my-Java-solution-using-dynamic-programming)

---

### 6. ZigZag Conversion

#### Round1

根据char的index找规律，最终有一个公式能计算出特定index上char对应的新位置（所在行和列)。

延伸问题，如何按照ZigZag打印一个字符串。

---

### 7. Reverse Integer

### Round1

常规做法，关键是如何处理溢出的情况https://leetcode.com/problems/reverse-integer/discuss/4060/My-accepted-15-lines-of-code-for-Java

---

### 8. String to Integer(atoi)

#### Round1

atoi的含义是(ASCII to Int)

常规做法。

---

### 9.回文数

#### Round1

1. 常规做法。把所有位都提取出来，对比。

2. 双指针。提取一位，对比一位，即时停止，防止浪费。
3. 精巧做法：https://leetcode.com/problems/palindrome-number/discuss/5127/9-line-accepted-Java-code-without-the-need-of-handling-overflow

---

### 10. Regular Express Matching

#### Round1

1. 递归的做法，所有的一种是普通的字符串对字符串的情况。一种是pattern第二个字符是*号的情况。

   *号的情况，可以拆分为 star的不再匹配任何字符，也可以匹配一个字符后，star继续投入匹配。

2. 因为该问题又最优子结构，所以可以用DP算法。

https://leetcode.com/problems/regular-expression-matching/solution/