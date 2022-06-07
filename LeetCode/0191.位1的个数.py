# -*- encoding: utf-8 -*-
'''
@File    :   0191.位1的个数.py
@Time    :   2022/06/05 21:20:27
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   

编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

 

提示：
请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/number-of-1-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    '''
    循环判断
    执行用时： 36 ms , 在所有 Python3 提交中击败了 76.51% 的用户 内存消耗： 14.8 MB , 在所有 Python3 提交中击败了 45.25% 的用户
    '''
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count


class Solution_better:
    '''
    n~\&~(n - 1)n & (n−1)，其运算结果恰为把 nn 的二进制位中的最低位的 11 变为 00 之后的结果
    '''
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            n &= n - 1
            ret += 1
        return ret
