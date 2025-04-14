## N
## Idea, approach and time complexity:
'''
The given code implements the **Longest Common Subsequence (LCS)** problem using **Dynamic Programming (DP)**. The idea is to build a 2D DP table `t` where `t[i][j]` 
represents the length of the LCS of the first `i` characters of `text1` and the first `j` characters of `text2`. If the characters `text1[i-1]` and `text2[j-1]` match, 
we add 1 to the result from `t[i-1][j-1]`; otherwise, we take the maximum value between `t[i-1][j]` and `t[i][j-1]`. This ensures we explore all possible subsequence 
combinations in an optimized manner. The **time complexity** is **O(m × n)**, where `m` and `n` are the lengths of `text1` and `text2` respectively, as we fill an `m+1` 
by `n+1` table. The **space complexity** is also **O(m × n)** due to the DP table.
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        t=[[0 for _ in range(n+1)] for _ in range(m+1)]
        for a in range(1,m+1):
            for b in range(1,n+1):
                if(text1[a-1]==text2[b-1]):
                    t[a][b]=1+t[a-1][b-1]
                else:
                    t[a][b]=max(t[a-1][b],t[a][b-1])
        return t[m][n]