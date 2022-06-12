# -*- encoding: utf-8 -*-
'''
@File    :   JZOF.58.II.左旋转字符串.py
@Time    :   2022/06/08 22:04:28
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = ""
        for i in range(n, n + len(s)):
            res += s[i % len(s)]
        return res


class Solution:
    '''
    执行用时： 32 ms , 在所有 Python3 提交中击败了 92.32% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 32.42% 的用户
    '''
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]