# -*- encoding: utf-8 -*-
'''
@File    :   JZOF.06.从尾到头打印链表.py
@Time    :   2022/06/08 16:58:14
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    执行用时： 32 ms , 在所有 Python3 提交中击败了 98.48% 的用户 内存消耗： 16.6 MB , 在所有 Python3 提交中击败了 51.75% 的用户
    """
    def reversePrint(self, head: ListNode) -> List[int]:
        ptr = head
        result = []
        while ptr:
            result.append(ptr.val)
            ptr = ptr.next
        result.reverse()
        return result