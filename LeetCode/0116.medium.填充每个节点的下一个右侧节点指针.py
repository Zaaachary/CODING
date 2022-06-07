# -*- encoding: utf-8 -*-
'''
@File    :   0116.medium.填充每个节点的下一个右侧节点指针.py
@Time    :   2022/03/06 15:31:55
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

'''
from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque

class Solution:
    '''
    64ms 62.17%  层序遍历记录层数；记录prior，连接线索二叉树
    '''
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = deque([root, '#'])

        prior_node = None
        while queue:
            current = queue.popleft()
            if prior_node:
                prior_node.next = current
            prior_node = current

            if current.left:
                queue.append(current.left)
                queue.append(current.right)

            if queue[0] == "#":
                current.next = None
                prior_node = None
                queue.popleft()
                if queue:
                    queue.append('#')

        return root