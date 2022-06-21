# -*- encoding: utf-8 -*-
'''
@File    :   JZOF.26.树的子结构.py
@Time    :   2022/06/20 19:22:31
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”


'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    执行用时： 80 ms , 在所有 Python3 提交中击败了 99.32% 的用户 内存消耗： 19.6 MB , 在所有 Python3 提交中击败了 17.45% 的用户
    '''
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B or not A:
            return False
        elif self.recur(A, B):
            return True
        else:
            return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    @staticmethod
    def recur(A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return True
        elif not A or A.val != B.val:
            return False
        else:
            return Solution.recur(A.left, B.left) and Solution.recur(A.right, B.right)

            