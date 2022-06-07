# -*- encoding: utf-8 -*-
'''
@File    :   0136.只出现一次的数字.py
@Time    :   2022/06/05 20:30:47
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

额外空间
1. hash 表  字典
2. 集合 set
3. 集合之和 *2 - 所有元素之和

不使用额外空间
异或
3 ^ 3 = 0
'''

class Solution:
    '''
    执行用时： 28 ms , 在所有 Python3 提交中击败了 99.87% 的用户 内存消耗： 16.8 MB , 在所有 Python3 提交中击败了 82.05% 的用户
    '''
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for item in nums:
            result ^= item
        return result

class Solution_better:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

