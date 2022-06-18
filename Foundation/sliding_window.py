# -*- encoding: utf-8 -*-
'''
@File    :   sliding_window.py
@Time    :   2022/06/17 15:47:57
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   滑动窗口模板
'''


# 模板一，需要记录变量个数
# 1004.最大连续1的个数 III
class Solution:
    def slidingWindow(nums, k):
        n = len(nums)
        #双指针，表示当前遍历的区间[left, right]，闭区间
        left = right = 0
        #定义变量统计 子数组/子区间 是否有效
        sum = 0
        #定义变量动态保存最大 求和/计数
        res = 0

        #右指针遍历到数组尾
        while right < n:
            #增加当前右指针对应的数值
            sum += nums[right]
            #当在该区间内 sum 超出定义范围
            while sum > k:
                #先将左指针指向的数值减去
                sum -= nums[left]
                #左指针右移
                left += 1
            #到 while 结束时，我们找到了一个符合题意要求的 子数组/子串
            res = max(res, right - left + 1)
            # 移动右指针，去探索下一个区间
            right += 1
        return res

## 模板二 适用于需要用 [哈希表] 记录的情况
# 567.字符串的排列、438.找到字符串中所有字母异位词

class Solution:
    def slidingWindow(s:str, t:str):
        #创建两个哈希表，分别记录 [需要的] 和 [加入的]
        # Map<Character, Integer> need = new HashMap<>();
        # Map<Character, Integer> map = new HashMap<>();
        need = {}
        map = {}

        #创建 [双指针] 和 [有效数量]
        left = right = 0
        valid = 0

        #外层循环，供右指针遍历
        while right < len(s):
            #创建临时 c 字符，是移入 窗口 内的字符
            ch = s[right]
            
            #进行窗口一系列逻辑更新
            ...
            
            #判断左指针是否要右移即窗口收缩：有效数量足够满足条件
            #  /*  可能是规定的窗口大小超出了，可能是有效值数量达成了
            #  1.  while(valid == need.size())
            #  2.  while(right - left + 1 >= s1.length())      
            #  */           
            while(windows need shrink){
                # 创建 d 是要移除窗口的字符
                char d = s.charAt(left);
                left+=1

                #进行窗口一系列逻辑更新
                ...
            }
            
            #右指针右移
            right+=1
        }
    }
}

