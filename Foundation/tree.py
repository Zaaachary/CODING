# -*- encoding: utf-8 -*-
'''
@File    :   tree.py
@Time    :   2021/12/13 22:49:08
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   
'''
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    @classmethod
    def build_tree(cls, node_list:List):
        """
        后序遍历 node_list 遍历过程中建树
        """
        node_list.insert(0, None)
        index = 1
        node_stack = []
        target = 1
        while target < len(node_list):
            node_stack.append(target)
            target = target * 2
        # TODO 树也需要一个堆栈
        last_visit = -1
        last_visit_tree = None
        while len(node_stack) != 0:
            node = node_stack[-1]
            right = node*2 + 1
            if right < len(node_list) and node_list[right] != None and last_visit == right-1:
                # 存在右节点且未被访问，上次访问的为该节点的左孩子
                
                target = right
                while target < len(node_list):
                    node_stack.append(target)
                    target = target * 2
                last_visit = -1
                last_visit_tree = None

            else:
                # 不存在右节点 或右节点已被访问，访问当前节点
                node_stack.pop(0)
                value = node_list[node]
                tree_node = cls(value)
                if last_visit == right:
                    # 右节点已访问
                    tree_node.right = last_visit_tree
                else:
                    # 无右节点，上次访问的为该节点的左孩子
                    tree_node.left = last_visit_tree
               


def X_order_traverse(p: 'TreeNode'):
    '''递归 X序遍历（pre, in, post）'''
    if p:
        # pre order visit(p)
        X_order_traverse(p.left)
        # In order  visit(p)
        X_order_traverse(p.right)
        # post order visit(p)


def pre_order_traverse(root: 'TreeNode'):
    '''迭代 先序遍历: 根入栈;出栈（访问;右左依次入栈）'''
    stack = []
    if root:
        stack.append(root)
    
    while len(stack) != 0:
        p = stack.pop()
        # visit(p)
        if p.right:
            stack.append(p.right)
        if p.left:
            stack.append(p.left)