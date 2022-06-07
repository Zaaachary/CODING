"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口 72ms 77.35%
        if len(s) == 0:
            return 0
        ans = f = 0
        for r in range(0, len(s)):
            if s[r] not in s[f:r]:
                ans = max(ans, r-f+1)
            else:
                while s[r] in s[f:r]:
                    f += 1
        # print(s[f:r+1])
        return ans

class Solution_1:
    '''
    60ms 73.41%
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, cur_len = 0, 0
        current_dict = {}   # 0: already appear; 1&None: not appear
        left, right = 0, 0
        while right < len(s):
            right_ch = s[right]
            if current_dict.get(right_ch, 1):
                current_dict[right_ch] = 0
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                while s[left] != right_ch:
                    current_dict[s[left]] = 1
                    left += 1
                    cur_len -= 1
                left += 1

            right += 1
        return max_len
            

if __name__ == "__main__":
    S = Solution()
    # test = "bbbb"
    # test = "abcabcbb"
    test = "pwwkew"
    print(S.lengthOfLongestSubstring(test))