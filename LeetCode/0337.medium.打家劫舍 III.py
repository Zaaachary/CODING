# -*- encoding: utf-8 -*-
'''
@File    :   0337.medium.打家劫舍 III.py
@Time    :   2022/07/13 20:14:53
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/house-robber-iii/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        wl, wol = self.max_val(root.left)        
        wr, wor = self.max_val(root.right)
        
        return max(wl + wr, wol + wor + root.val)

    def max_val(self, root):
        '''
        with current, without current
        '''
        if not root:
            return 0, 0
        else:
            wl, wol = self.max_val(root.left)        
            wr, wor = self.max_val(root.right)
            
            return max(wol + wor + root.val, wl + wr), wl + wr