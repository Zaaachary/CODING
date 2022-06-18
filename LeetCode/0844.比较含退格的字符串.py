# -*- encoding: utf-8 -*-
'''
@File    :   0844.比较含退格的字符串.py
@Time    :   2022/06/16 14:08:09
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   

给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/backspace-string-compare
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    '''
    双指针比较两个字符串
    执行用时： 28 ms , 在所有 Python3 提交中击败了 98.49% 的用户 内存消耗： 15 MB , 在所有 Python3 提交中击败了 31.69% 的用户
    '''
    def backspaceCompare(self, s: str, t: str) -> bool:
        ptr1 = len(s) - 1
        ptr2 = len(t) - 1
        
        while ptr1 >= 0 or ptr2 >= 0:
            # import pdb; pdb.set_trace()
            skip =  0
            while ptr1 >= 0:
                if s[ptr1] == '#':
                    skip += 1
                    ptr1 -= 1
                elif skip > 0:
                    ptr1 -= 1
                    skip -= 1
                else:
                    break
            skip =  0
            while ptr2 >= 0:
                if t[ptr2] == '#':
                    skip += 1
                    ptr2 -= 1
                elif skip > 0:
                    ptr2 -= 1
                    skip -= 1
                else:
                    break
            # import pdb; pdb.set_trace()
            
            if ptr1 >= 0 and ptr2 >= 0:
                if s[ptr1] != t[ptr2]:
                    return False
            elif ptr1 >= 0 or ptr2 >= 0:
                return False
            ptr1 -= 1
            ptr2 -= 1
        return True

class Solution_old:
    '''
    两年前写的骚东西
    '''
    def backspaceCompare(self, S: str, T: str) -> bool:
        # 反向遍历 双指针
        import itertools
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))


class Solution_stack:

    '''
    stack
    执行用时： 36 ms , 在所有 Python3 提交中击败了 75.37% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 14.12% 的用户 通过测试用例： 114 / 114
    '''
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_1, stack_2 = [], []
        for ch in s:
            if ch != '#':
                stack_1.append(ch)
            else:
                stack_1.pop()
        for ch in t:
            if ch != '#':
                stack_2.append(ch)
            else:
                stack_2.pop()
        return True if ''.join(stack_1) == ''.join(stack_2) else False


if __name__ == "__main__":
    S = Solution()
    source = 'bxj##tw'
    target = 'bxo#j##tw'
    print(S.backspaceCompare(source, target))
    