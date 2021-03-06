
"""
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-bad-version
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    '''
    执行用时： 32 ms , 在所有 Python3 提交中击败了 87.38% 的用户 内存消耗： 14.9 MB , 在所有 Python3 提交中击败了 31.47% 的用户
    '''
    def firstBadVersion(self, n):
        left, right = 1, n
        first =  n + 1
        while left <= right:
            mid = (right - left) // 2 + left
            if isBadVersion(mid):
                first = min(first, mid)
                right = mid - 1
            else:
                left = mid + 1
        return first

class Solution_better:
    def firstBadVersion(self, n):
        '''
        目标是最后left和right收缩到错误的第一个版本
        '''
        left, right = 1, n
        while left < right:
            mid = (right - left) // 2 + left
            if isBadVersion(mid):
                right = mid # not mid -1
            else:
                left = mid + 1

        return left
