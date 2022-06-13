# -*- encoding: utf-8 -*-
'''
@File    :   JZOF.24.反转链表.py
@Time    :   2022/06/08 17:02:18
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   和 206题目相同
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。


'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    执行用时： 36 ms , 在所有 Python3 提交中击败了 87.02% 的用户 内存消耗： 16 MB , 在所有 Python3 提交中击败了 80.67% 的用户
    '''
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            temp = head
            head = head.next

            temp.next = new_head
            new_head = temp

        return new_head

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