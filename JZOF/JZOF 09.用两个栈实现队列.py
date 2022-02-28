# -*- encoding: utf-8 -*-
'''
@File    :   Offer 09.用两个栈实现队列.py
@Time    :   2022/01/10 14:37:43
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
'''

class CQueue_method_1:
    """
    执行用时： 400 ms , 在所有 Python3 提交中击败了 24.21% 的用户
    内存消耗： 18.8 MB , 在所有 Python3 提交中击败了 9.45% 的用户
    """

    def __init__(self):
        self.total_len = 0
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        # stack 1 is not full -> append stack 1 (in python, will not full)
        # stack 1 is full and stack 2 is empty -> trans item from stack 1 to stack 2, then append item to stack 1
        # stack 1 is full and stack 2 is not empty -> queue full
        self.stack1.append(value)

    def deleteHead(self) -> int:
        # stack 2 is not empty -> pop item from stack 2
        # stack 2 is empty and stack 1 is empty -> return -1
        # stack 2 is empty and stack 1 is not empty -> trans item from stack 1 to stack 2, then pop item from stack 1
        if self.stack2:
            # stack 2 is not empty
            return self.stack2.pop()
        elif self.stack1:
            # stack 2 is empty, stack 1 is not empty
            self.stack2, self.stack1 = self.stack1, self.stack2
            self.stack2.reverse()
            return self.stack2.pop()
        else:
            # both are empty
            return -1

class CQueue_method_2:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()