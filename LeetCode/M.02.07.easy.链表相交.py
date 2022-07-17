# -*- encoding: utf-8 -*-
'''
@File    :   M.02.07.easy.链表相交.py
@Time    :   2022/07/15 23:12:08
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Solution 2
        '''
        执行用时： 140 ms , 在所有 Python3 提交中击败了 86.27% 的用户 内存消耗： 30.3 MB , 在所有 Python3 提交中击败了 5.15% 的用户
        '''
        Anode_set = set()
        ptr = headA
        while ptr:
            Anode_set.add(ptr)
            ptr = ptr.next
        
        ptr = headB
        while ptr:
            if ptr in Anode_set:
                return ptr
            ptr = ptr.next
        return None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        执行用时： 6876 ms , 在所有 Python3 提交中击败了 6.61% 的用户 内存消耗： 29.8 MB , 在所有 Python3 提交中击败了 76.26% 的用户
        '''
        Anodes = []
        ptr = headA
        while ptr:
            Anodes.append(ptr)
            ptr = ptr.next
        
        ptr = headB
        while ptr:
            for node in Anodes:
                if node == ptr:
                    return node
            ptr = ptr.next
        
        return None
