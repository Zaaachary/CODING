# -*- encoding: utf-8 -*-
'''
@File    :   0225.medium.用队列实现栈.py
@Time    :   2022/07/13 21:16:34
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/implement-stack-using-queues/
'''

from collections import deque

class MyStack:

    '''
    执行用时： 32 ms , 在所有 Python3 提交中击败了 87.61% 的用户 内存消耗： 15.2 MB , 在所有 Python3 提交中击败了 5.01% 的用户
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1


class MyStack:

    '''
    执行用时： 40 ms , 在所有 Python3 提交中击败了 39.66% 的用户 内存消耗： 15.2 MB , 在所有 Python3 提交中击败了 10.55% 的用户
    '''
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        if self.queue2:
            self.queue2, self.queue1 = self.queue1, self.queue2
            self.queue1.reverse()            
        self.queue1.appendleft(x)

    def pop(self) -> int:
        
        if self.queue2:
            return self.queue2.pop()
        else:
            self.queue2, self.queue1 = self.queue1, self.queue2
            self.queue2.reverse()
            return self.queue2.pop()

    def top(self) -> int:
        # print(self.queue1, self.queue2)
        if self.queue2:
            return self.queue2[-1]
        elif self.queue1:
            self.queue2, self.queue1 = self.queue1, self.queue2
            self.queue2.reverse()
            return self.queue2[-1]
        else:
            return -1

    def empty(self) -> bool:
        if self.queue1 or self.queue2:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
