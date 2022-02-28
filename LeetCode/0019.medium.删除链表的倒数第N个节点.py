# -*- encoding: utf-8 -*-
'''
@File    :   0019.删除链表的倒数第N个节点.medium.py
@Time    :   2022/01/05 22:42:04
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    32ms 击败 84.15%
    fake head node + slow fast double ptr
    '''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fake_head = ListNode()
        fake_head.next = head

        slow = fast = fake_head  # index the prior of target node
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        temp = slow.next
        slow.next = temp.next
        del temp

        return fake_head.next
