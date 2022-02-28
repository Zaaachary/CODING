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

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_item = None
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_item

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()