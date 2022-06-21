# -*- encoding: utf-8 -*-
'''
@File    :   0117.medium.填充每个节点的下一个右侧节点指针.py
@Time    :   2022/06/21 17:16:34
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''


class Solution:
    '''
    执行用时： 52 ms , 在所有 Python3 提交中击败了 73.33% 的用户 内存消耗： 16.5 MB , 在所有 Python3 提交中击败了 5.19% 的用户
    '''
    def connect(self, root: 'Node') -> 'Node':
        queue = []
        prev, end = None, root
        if root:
            queue.append(root)
            queue.append(None)

        while queue:
            current = queue.pop(0)
            if prev:
                prev.next = current
            prev = current
            if current:
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            elif len(queue) >= 1:
                queue.append(None)
                    
        return root