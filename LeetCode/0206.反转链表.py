# -*- encoding: utf-8 -*-
'''
@File    :   206.反转链表.py
@Time    :   2022/02/21 09:40:01
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_dd:
    '''
    迭代  32ms 88.46%
    '''
    def reverseList1(self, head: ListNode) -> ListNode:
        prior = None
        current = head
        while current:
            current_next = current.next
            current.next = prior
            prior = current
            current = current_next

        return prior


class Solution_dg:

    def reverseList_1(self, head: ListNode, head_prior=None) -> ListNode:
        '''
        递归 24ms  99.37%; 20.5MB 9.74%
        O(n)  O(n)
        '''
        if not head:
            return head_prior
        else:
            head_next = head.next
            head.next = head_prior

            return self.reverseList(head_next, head)

    def reverseList_2(self, head: ListNode) -> ListNode:
        '''
        60ms 7.84% 20.6 9.37%
        在1 的基础上调整了递归的顺序，取消尾递归，性能退化
        '''
        if not head or not head.next:
            return head
        else:
            # head 之后的节点反转，并返回新的头
            new_head = self.reverseList(head.next)
            # head 的下一节点指向 head
            head.next.next = head
            head.next = None

            return new_head