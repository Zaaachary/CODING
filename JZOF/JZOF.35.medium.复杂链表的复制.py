# -*- encoding: utf-8 -*-
'''
@File    :   JZOF.35.复杂链表的复制.py
@Time    :   2022/06/08 19:23:26
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

same as 138

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    '''
    执行用时： 28 ms , 在所有 Python3 提交中击败了 99.79% 的用户 内存消耗： 16.3 MB , 在所有 Python3 提交中击败了 6.94% 的用户
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
