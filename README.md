# CODING

[TOC]

[力扣 20天算法刷题 计划](https://leetcode-cn.com/study-plan/algorithms/?progress=2mj8onm)

[代码随想录](https://www.programmercarl.com/)

## 1 数据结构

### 1.1 栈


### 1.2 树

- 236 递归设计(妙) / 后序遍历
- 617 easy 合并二叉树
- 116 medium 填充每个节点的下一个右侧节点指针；线索二叉树

## 2 常见算法

### 2.1 二分查找

- 704 easy 最基本形式
- 278 easy 第一个错误版本(变体)
- 035 easy 搜索插入位置

### 2.2 双指针

- 977 easy 有序数组的平方，前后向中遍历/前后归并
- 189 medium 轮转数组；环状替换 整体翻转前后分别翻转 / 数学解
- 283 easy 移动零；区域指针
- 167 medium 两数之和II 快慢指针找中间节点
- 019 medium 删除链表的倒数第N个节点 快慢指针找倒数第N个节点
- 876 easy 链表的中间
- 167 medium 两数之和；左右筛选
- 344 easy 反转字符串
- 557 easy 反转字符串中的单词

### 2.3 滑动窗口

- 003 medium 无重复字符的最长字串
- 567 medium 字符串的排列；优化方法待看 TODO


### 2.4 广度/深度优先搜索

有规则的数据遍历，图、树、数组

- TODO 递归的广度/深度优先搜索 and 非递归广度/深度优先搜索的标准写法
- 733 easy 图像渲染；搜索+可以不用visited
- 695 medium 岛屿的最大面积； 优化：根据并修改grid值 不适用visited
- 617 easy 合并二叉树
- 116 medium 填充每个节点的下一个右侧节点指针；层序遍历记录层数；记录prior，连接线索二叉树
- 542 medium 01矩阵；超级源点，广度优先遍历，但首先添加所有0； 动态规划 四个方向更新四遍
- 994 medium todo

### 2.5 递归/回溯

- 021 easy 合并两个有序链表
- 206 easy 反转链表  迭代/递归，递归可改造尾递归
- 077 medium ! 组合，递归； [dfs 回溯法+剪枝]
- 046 medium ! 全排列，DFS回溯法，  todo 优化题解
- 784 medium 字母大小写全排列 todo

### 2.6 动态规划

- TBD

### 2.7 位运算

- 190

### 2.8 TODO

- 最大公约数GCD

- 913 hard; 动态规划 & 博弈; 未做出


## 3 实用标准库

1. itertools
    - combinations  组合
    - permutations  排列
