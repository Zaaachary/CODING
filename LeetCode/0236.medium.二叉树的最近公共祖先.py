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
from collections import Counter


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        48ms 99.29%
        https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/c-jing-dian-di-gui-si-lu-fei-chang-hao-li-jie-shi-/
        
        递归目标:
        - 当前树存在 pq 则返回公共祖先
        - 仅存在一个，则返回存在的一个节点
        - 都不存在则返回 None

        """
        if not root:
            return None
        
        if root == p or root == q:
            # 当前节点为 p 或 q
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)

            if not left:
                # 左侧无p无q，则右侧为返回的公共祖先
                return right
            elif not right:
                # 右侧无p无q，则左侧为返回的公共祖先
                return left
            else:
                # p 和 q 在当前节点两侧，当前节点为最近的公共祖先
                return root


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        64ms  64.36%
        后续遍历，找到 p 时记录堆栈祖先，找到 q 时记录堆栈祖先，通过比较堆栈找到最近祖先。
        """
        path1 = Solution.post_traverse_find(root, p)
        path2 = Solution.post_traverse_find(root, q)
        count = Counter(path1 + path2)
        for node in path1:
            if count[node] == 2:
                return node

    @staticmethod
    def post_traverse_find(root, target):
        node_stack = []
        last_visit = None
        while root:
            node_stack.append(root)
            root = root.left

        while len(node_stack) != 0:
            # node 无左孩子或左孩子已经被访问
            node = node_stack[-1]
            if node == target:
                # print(node.val)
                return node_stack

            if node.right and last_visit != node.right:
                # 有右孩子，且未被访问
                node = node.right
                while node:
                    # 右孩子及其左孩子链入栈
                    node_stack.append(node)
                    node = node.left
            else:
                # 没有右孩子，或有右孩子已经被访问
                last_visit = node_stack.pop()
                
if __name__ == "__main__":
    # TreeNode.build_tree([1,2,3])
    pass
            
        
        
        
