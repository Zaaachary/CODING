# -*- encoding: utf-8 -*-
'''
@File    :   JZOF 30.包含min函数的栈.py
@Time    :   2022/01/10 15:55:07
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
'''

class MinStack:
    '''
    假设栈内元素单调增，将打破单调增且小于最小栈top的元素存入最小栈
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mini = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        # 最小栈为空 或者 新插入的元素不大于最小栈栈顶
        if not self.mini or x <= self.mini[-1]:
            self.mini.append(x)


    def pop(self) -> None:
        # 最小栈不为空，且主栈出的元素和最小栈顶相同
        if self.mini and self.stack[-1] == self.mini[-1]:
            self.mini.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]


    def min(self) -> int:
        if self.mini:
            return self.mini[-1]
        else:
            return None


class MinStack_1:
    '''
    和 stack 等大小的辅助栈
    执行用时： 56 ms , 在所有 Python3 提交中击败了 85.34% 的用户 内存消耗： 18.9 MB , 在所有 Python3 提交中击败了 5.04% 的用户
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [float("inf"),]

    def push(self, x: int) -> None:
        self.min_stack.append(min(self.min_stack[-1], x))
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
S = MinStack()
import pdb; pdb.set_trace()