# -*- encoding: utf-8 -*-
'''
@File    :   0876.链表的中间节点.py
@Time    :   2022/01/05 22:03:28
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_new:
    '''
    2022/0228  36ms 48%
    '''
    def middleNode(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        时间复杂度 O(n) 空间 O(1)
        28ms 击败了88.92%
        快的能走慢的就走，快指针到头后慢指针，根据最后快指针走的步数决定慢指针是否需要补走。
        """
        fake_head = ListNode()
        fake_head.next = head

        fast_ptr = slow_ptr = fake_head
        
        fast_last_move_two = False
        while slow_ptr.next:
            if fast_ptr.next:
                fast_ptr = fast_ptr.next
                if fast_ptr.next:
                    fast_ptr = fast_ptr.next
                    fast_last_move_two = True
                else:
                    fast_last_move_two = False
                slow_ptr = slow_ptr.next
            else:
                break
        if fast_last_move_two:
            slow_ptr = slow_ptr.next
        return slow_ptr

class Solution_2:
    '''
    不使用假头节点，记录快指针移动奇偶次数。
    达到2则移动慢指针，特殊case为快指针移动单次，慢指针移动1次。
    '''
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        count = 0
        while fast.next is not None:
            fast = fast.next
            count += 1
            if count == 2:
                count = 0
                slow = slow.next
        else:
            if count == 1:
                slow = slow.next


        return slow


