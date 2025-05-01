## N
## Idea, approach and time complexity:
'''
The given solution is designed to find the length of the longest palindromic subsequence in a string. The core idea is based on the observation that a palindrome reads 
the same forward and backward, so the longest palindromic subsequence in a string `s` is equivalent to the longest common subsequence (LCS) between `s` and its reverse 
`s[::-1]`. The `lcs` function implements the classic dynamic programming approach to compute the LCS by building a 2D table `t`, where `t[i][j]` stores the LCS of the 
first `i` characters of `s1` and the first `j` characters of `s2`. When characters match, the current LCS extends the LCS from the previous indices; otherwise, it takes 
the longer of the two possible subsequences. After filling the table, the LCS of the entire strings is found at `t[m][n]`, and its length gives the result. The time 
complexity of this approach is **O(n²)**, where `n` is the length of the input string, due to the nested loops filling in an `n x n` table. The space complexity is also 
**O(n²)** because of the 2D DP table storing strings.
'''

class Solution:
    def lcs(self,s1,s2,m,n):
        t=[["" for _ in range(n+1)] for _ in range(m+1)]
        for a in range(1,m+1):
            for b in range(1,n+1):
                if(s1[a-1]==s2[b-1]):
                    t[a][b]=t[a-1][b-1]+s1[a-1]
                else:
                    lcs1,lcs2=t[a-1][b],t[a][b-1]
                    t[a][b]=lcs1 if len(lcs1)>len(lcs2) else lcs2
        return t[m][n]

    def longestPalindromeSubseq(self, s: str) -> int:
        s1,s2=s,s[::-1]
        m,n=len(s1),len(s2)
        return len(self.lcs(s1,s2,m,n))