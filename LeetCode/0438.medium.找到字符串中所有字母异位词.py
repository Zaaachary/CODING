# -*- encoding: utf-8 -*-
'''
@File    :   438.找到字符串中所有字母异位词.py
@Time    :   2022/06/16 17:27:47
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   

'''
from typing import List
from collections import Counter
from copy import deepcopy

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1

        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)

        for i in range(s_len - p_len):
            if count[ord(s[i]) - 97] == 1:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i]) - 97] -= 1

            if count[ord(s[i + p_len]) - 97] == -1:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i + p_len]) - 97] == 0:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i + p_len]) - 97] += 1
            
            if differ == 0:
                ans.append(i + 1)

        return ans

class Solution:
    '''
    优化版本，不使用 deepcopy
    执行用时： 84 ms , 在所有 Python3 提交中击败了 78.40% 的用户 内存消耗： 15.8 MB , 在所有 Python3 提交中击败了 5.61% 的用户
    '''
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(p) > len(s):
            return result
        target_dict = Counter(p)

        current_len, target_len = 0, len(p)
        left, right = 0, 0
        while right < len(s):
            temp = s[right]
            free_num = target_dict.get(temp, -1)
            if free_num > 0:
                target_dict[temp] -= 1
                current_len += 1
                if current_len == target_len:
                    result.append(left)
                    target_dict[s[left]] += 1
                    left += 1
                    current_len -= 1
                right += 1
            elif free_num == 0 and left != right:
                target_dict[s[left]] += 1
                left += 1
                current_len -= 1
            else:
                while left < right:
                    target_dict[s[left]] += 1
                    left += 1
                left = right + 1
                current_len = 0
                right = left
        return result


class Solution_v1:
    '''
    执行用时：448 ms, 在所有 Python3 提交中击败了13.06%的用户 内存消耗：15.8 MB, 在所有 Python3 提交中击败了5.30%的用户
    '''
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(p) > len(s):
            return result
        target_dict = Counter(p)
        current_dict = deepcopy(target_dict)

        current_len, target_len = 0, len(p)
        left, right = 0, 0
        while right < len(s):
            temp = s[right]
            free_num = current_dict.get(temp, -1)
            if free_num > 0:
                current_dict[temp] -= 1
                current_len += 1
                if current_len == target_len:
                    result.append(left)
                    current_dict[s[left]] += 1
                    left += 1
                    current_len -= 1
                right += 1
            elif free_num == 0 and left != right:
                current_dict[s[left]] += 1
                left += 1
                current_len -= 1
            else:
                left = right + 1
                current_dict = deepcopy(target_dict)
                current_len = 0
                right = left
        return result
            
class Solution_vio:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        
        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            
            if s_count == p_count:
                ans.append(i + 1)

        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.findAnagrams("cbaebabacd","abc"))