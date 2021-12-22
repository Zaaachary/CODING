# -*- encoding: utf-8 -*-
'''
@File    :   0236.二叉树的最近公共祖先.py
@Time    :   2021/11/30 15:48:03
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：
“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
'''

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
<<<<<<< HEAD
    
=======
        
>>>>>>> 7c53f016f25f99c08955cd1ee2a4f3e60d2f0f95

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        后续遍历，找到 p 时记录堆栈祖先，找到 q 时记录堆栈祖先，通过比较堆栈找到最近祖先。
        """
        pass

    @staticmethod
    def post_traverse(root):
        node_stack = []
        last_visit = None
        while root:
            node_stack.append(root)
            root = root.left

        while len(node_stack) != 0:
            # node 无左孩子或左孩子已经被访问
            node = node_stack[-1]
            if node.right and last_visit == node.left:
                # 有右孩子，且左孩子刚被访问
                node = node.right
                while node:
                    # 右孩子及其左孩子链入栈
                    node_stack.append(node)
                    node = node.left
            else:
                # 没有右孩子，或有右孩子已经被访问
                last_visit = node_stack.pop(0)
                print(last_visit.data)
                
if __name__ == "__main__":
    TreeNode.build_tree([1,2,3])
            
        
        
        
