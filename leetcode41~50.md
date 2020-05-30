### 41. First Missing Positive

#### Round1

假设数组长度为L, 找到小于L的正整数A，把其放到位置A-1上。

跌倒数组找到位置和值不匹配的第一个值。

---

### 42. Trapping Rain Water

### Round1

这道题的方法是逐个的计算每个格子的蓄水量，然后相叠加。

每个格子的蓄水量为Min(Rmax - Lmax) - Height[i]

基于这个方案，于是有三种方案：

1. broute
2. dp
3. two pointer

dp和two_pointer都是为了加速求出Rmax和Lmax

不过双指针，更加精巧。他利用的隐藏信息更多。

法四：栈的方法。

---

### 43. Multiply Strings

#### Round1

逐字符相乘。字符转为数字使用ord()

---

### 44. Wildcard Matching

#### Round1

递归，迭代，头部模式。

---

### 45. Jump Game II

#### Round1

动态规划。

---

### 45. Permutations

#### Round1

backTrace

---

### 47. Permutations II

#### Round1

backTrace, backTrace之前排序。

要注意重复数字的处理。

---

### 48. Rotate Image

#### Round1

空间转换问题，把难的操作变为简单操作。

---

### 49. Group Anagrams

#### Round1

能直接想起来的当然是暴力了，但是我不想暴力。

我能想到的是把字符串按照字符排序。

---

### 50. Pow(x, n)

#### Round1

最简单的解法当然是暴力解法。
但是考虑pow(0.001, 100000)的情况呢？
所以要用二分法