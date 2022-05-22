# -*- encoding: utf-8 -*-
'''
@File    :   0002.两数相加.py
@Time    :   2022/05/21 22:48:58
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    执行用时： 52 ms , 在所有 Python3 提交中击败了 96.48% 的用户 内存消耗： 14.9 MB , 在所有 Python3 提交中击败了 81.59% 的用户
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fake_head = ListNode(-1)
        ptr = fake_head
        carry  = 0
        while l1 or l2 or carry:
            new_val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, new_val = divmod(new_val, 10)    
            ptr.next = ListNode(new_val)
            ptr = ptr.next
        return fake_head.next


class Solution_1:
    """执行用时： 60 ms , 在所有 Python3 提交中击败了 73.82% 的用户 内存消耗： 14.9 MB , 在所有 Python3 提交中击败了 76.94% 的用户"""
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        ptr = head
        add_up = 0
        while l1 or l2:
            if l1 and l2:
                temp = l1.val + l2.val + add_up
                add_up = 0
                l1 = l1.next
                l2 = l2.next
            elif l1:
                temp = l1.val + add_up
                add_up = 0
                l1 = l1.next
            elif l2:
                temp = l2.val + add_up
                l2 = l2.next
                add_up = 0
            if temp >= 10:
                temp -= 10
                add_up = 1
            ptr.next = ListNode(temp)
            ptr = ptr.next
        else:
            if add_up:
                ptr.next = ListNode(1)


        return head.next