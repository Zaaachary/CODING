# -*- encoding: utf-8 -*-
'''
@File    :   0082.medium.删除排序链表中的重复元素 II.py
@Time    :   2022/06/13 15:25:17
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   

给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序 排列
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    执行用时： 40 ms , 在所有 Python3 提交中击败了 89.71% 的用户 内存消耗： 15 MB , 在所有 Python3 提交中击败了 65.98% 的用户
    '''
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_node = ListNode(-1, head)

        ptr = head
        prev = dummy_node
        while ptr:
            current_val = ptr.val
            if ptr.next and ptr.next.val == current_val:
                while ptr and ptr.val == current_val:
                    prev.next = ptr.next
                    del ptr
                    ptr = prev.next
            else:
                prev = ptr
                ptr = ptr.next

        return dummy_node.next

