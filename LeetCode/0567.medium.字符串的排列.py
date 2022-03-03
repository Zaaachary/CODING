# -*- encoding: utf-8 -*-
'''
@File    :   0567.medium.字符串的排列.py
@Time    :   2022/02/28 16:04:20
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   
'''

from collections import Counter

class Solution:
    '''
    2022/0228  116ms  32.86%
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_dict = Counter(s1)
        left = 0
        current_len = 0
        for right, right_ch in enumerate(s2):
            free_num = s1_dict.get(right_ch, -1)
            if free_num > 0:
                s1_dict[right_ch] -= 1
                current_len += 1
                if current_len == len(s1):
                    return True
            elif free_num == -1:
                # right_ch not in s1
                left = right + 1
                current_len = 0
                s1_dict = Counter(s1)
            else:
                # s2[left:right+1] is not the substring of s1's premutation
                while s2[left] != right_ch and left < right:
                    s1_dict[s2[left]] += 1
                    left += 1
                    current_len -= 1
                left += 1

        return False

from collections import defaultdict

class Solution_fast:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = defaultdict(int)
        for i in s1:
            dic[i]+=1
        left= 0
        n=0
        for right in range(len(s2)):
            if s2[right] in s1:
                if dic[s2[right]]>0:
                    n+=1
                dic[s2[right]]-=1
            if n == len(s1):
                while right-left+1>len(s1):
                    if s2[left] in s1:
                        if dic[s2[left]]>=0:
                            n-=1
                        dic[s2[left]]+=1
                    left+=1
                if n == len(s1):
                    return True
                
        return False




if __name__ == "__main__":
    S = Solution()
    print(S.checkInclusion("ab", "acb"))