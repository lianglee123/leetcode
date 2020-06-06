### 71. Simplify Path

#### Round1

使用堆栈

---

### 72. Edit Distance

#### Round1

看似是使用DP, 其实最直观的是使用DFS, 然后使用DP优化DFS

---

### 73. Set Matrix Zeroes

#### Round1

暴力做肯定行，但是不体面。

我在做法是，使用一个map, 记录下每一个row/col的set 记录，避免重复处理。

#### Round2
真正的trick在于，上一行的更改，不能影响下一行的判断
如果引用set记录处理过的行，会导致内存变成o(m+n)
这里使用第一行和第一列作为 记录器。

---

### 74. Search a 2D Matrix

#### Round1

先二分法找到target可能所在行，再找到所在列

---

### 75. Sort Colors

#### Round1

双指针

---

### 76. Minimum Window Substring（Hard)

#### Round1



---

### 77. Combinations

#### Round1

回溯

---

### 78. Subsets

#### Round1

回溯？

---

### 79. Word Search

#### Round1

Fuck， 回溯+搜索