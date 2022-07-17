# -*- encoding: utf-8 -*-
'''
@File    :   0072.hard.!.编辑距离.py
@Time    :   2022/06/25 17:19:54
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   

在单词 A 中插入一个字符；
在单词 B 中插入一个字符；
修改单词 A 的一个字符。

'''

class Solution:
    '''
    执行用时： 140 ms , 在所有 Python3 提交中击败了 89.32% 的用户 内存消耗： 18.8 MB , 在所有 Python3 提交中击败了 39.06% 的用户
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp_matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for idx in range(m+1):
            dp_matrix[idx][0] = idx
        
        for idx in range(n+1):
            dp_matrix[0][idx] = idx

        for i in range(1, m+1):
            for j in range(1, n+1):
                j_1 = dp_matrix[i][j-1]     # 字符1 <-> 字符2[:-1] 编辑距离，接下来可做插入
                i_1 = dp_matrix[i-1][j]     # 字符1[:-1] <-> 字符2 编辑距离，接下来可做插入
                ij_1 = dp_matrix[i-1][j-1]  # 字符1[:-1] <-> 字符2[:-1] 编辑距离，接下来可做新字符交换

                if word2[j-1] == word1[i-1]:
                    dp_matrix[i][j] = min(j_1 + 1, i_1 + 1, ij_1)
                else:
                    dp_matrix[i][j] = 1 + min(j_1, i_1, ij_1)
        
        return dp_matrix[-1][-1]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]

from functools import cache

class Solution_memory:
    '''
    记忆化搜索
    执行用时： 756 ms , 在所有 Python3 提交中击败了 5.16% 的用户 内存消耗： 126.1 MB , 在所有 Python3 提交中击败了 5.01% 的用户
    '''
    @cache
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        elif not word1:
            return len(word2)
        elif not word2:
            return len(word1)
        
        mid_1 = self.minDistance(word1[:-1], word2) 
        mid_2 = self.minDistance(word1, word2[:-1])
        mid_3 = self.minDistance(word1[:-1], word2[:-1])
        if word1[-1] == word2[-1]:
            return 1 + min(mid_1, mid_2, mid_3 - 1)
        else:
            return 1 + min(mid_1, mid_2, mid_3)

if __name__ == "__main__":
    text1 = """
    There are two major concerns with the paper: contributions, and evaluation. First, the contributions of the paper are limited with respect to a large body of existing work. KERP's main pitch is the idea of injecting external knowledge into the BART/GPT2 language model for QA tasks. As the authors also discuss, this is not a new idea and there is a ton of research on it. The only distinction that the authors mention is on line 156: "rather than the direct evidence, we focus on gathering the commonsense background knowledge for the question.” which is again something that has been tried for years and there are tons of evidence that injecting relevant commonsense knowledge into the models will improve LMs performance. Just to name a few: KagNet (Lin, Bill Yuchen, et al. 2019), ERNIE (Zhang, Zhengyan, et al. 2019). So what is the contribution here? Is KERP's contribution just trying knowledge injection on a different task (ProtoQA)? The same issues are valid in the second and third contributions, where they are limited to and tailored toward ProtoQA tasks.
Second, the models selected for evaluation are pretty limited. Table 2 summarizes the main results of the evaluation on the ProtoQA tasks from the task's online leaderboard. The results show that KERP is beating SOTA in 3 out of 7 metrics (one "Inc@3” being the official ranking criteria). Even though the results on ”Inc@3” is pretty significant in the ProtoQA task, the mixed results make it difficult to draw any conclusion on the merits of KERP. Also, there is a huge body of work on improving language models in commonsense QA tasks by injecting knowledge. Just to name a few: UnifiedQA (Khashabi, Daniel, et al 2020 and 2022), HyKAS (Ma, Kaixin, et al. 2019). So even if we accept the limited focus of the paper on ProtoQA, one would expect to see the results in comparison with existing SOTA models in the task, not just relying on the ProtoQA leaderboard results.
    """

    text2 = """
    There are two major concerns with the paper: contributions, and evaluation. First, the contributions of the paper are limited with respect to a large body of existing work. KERP's main pitch is the idea of injecting external knowledge into the BART/GPT2 language model for QA tasks. As the authors also discuss, this is not a new idea and there is a ton of research on it. The only distinction that the authors mention is on line 156: "rather than the direct evidence, we focus on gathering the commonsense background knowledge for the question.” which is again something that has been tried for years and there are tons of evidence that injecting relevant commonsense knowledge into the models will improve LMs performance. Just to name a few: KagNet (Lin, Bill Yuchen, et al. 2019), ERNIE (Zhang, Zhengyan, et al. 2019). So what is the contribution here? Is KERP's contribution just trying knowledge injection on a different task (ProtoQA)? The same issues are valid in the second and third contributions, where they are limited to and tailored toward ProtoQA tasks.
Second, the models selected for evaluation are pretty limited. Table 2 summarizes the main results of the evaluation on the ProtoQA tasks from the task's online leaderboard. The results show that KERP is beating SOTA in 3 out of 7 metrics (one "Inc@3” being the official ranking criteria). Even though the results on ”Inc@3” is pretty significant in the ProtoQA task, the mixed results make it difficult to draw any conclusion on the merits of KERP. Also, there is a huge body of work on improving language models in commonsense QA tasks by injecting knowledge. Just to name a few: UnifiedQA (Khashabi, Daniel, et al 2020 and 2022), HyKAS (Ma, Kaixin, et al. 2019). So even if we accept the limited focus of the paper on ProtoQA, one would expect to see the results in comparison with existing SOTA models in the task, not just relying on the ProtoQA leaderboard results.
    """
    S = Solution()
    print(S.minDistance(text1, text2))