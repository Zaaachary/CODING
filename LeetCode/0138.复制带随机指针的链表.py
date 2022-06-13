# -*- encoding: utf-8 -*-
'''
@File    :   0138.复制带随机指针的链表.py
@Time    :   2022/06/08 19:26:20
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''

class Solution:
    '''
    执行用时： 40 ms , 在所有 Python3 提交中击败了 80.94% 的用户 内存消耗： 16.3 MB , 在所有 Python3 提交中击败了 17.23% 的用户
    '''
    def __init__(self):
        self.node_hash = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head:
            if head in self.node_hash:
                new_head = self.node_hash[head]
                return new_head
            else:
                new_head = Node(head.val)
                self.node_hash[head] = new_head
            new_head.next = self.copyRandomList(head.next)
            new_head.random = self.copyRandomList(head.random)
            return new_head
        else:
            return None