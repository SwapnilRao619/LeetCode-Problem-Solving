## N
## Idea, approach and time complexity:
'''
The given solution computes the **minimum number of deletions** required to make two strings equal by leveraging the **Longest Common Subsequence (LCS)**. The core idea 
is that characters not part of the LCS must be deleted from either string. The `lcs` method uses dynamic programming to build a 2D table that stores the actual LCS 
strings for all prefixes of `word1` and `word2`. Once the LCS is obtained, the number of deletions needed is the sum of the characters in both strings that are not part 
of the LCS, calculated as `(len(word1) - len(LCS)) + (len(word2) - len(LCS))`. The time and space complexity of the solution is **O(m × n)**, where `m` and `n` are the 
lengths of the two input strings, due to the nested loops and 2D table storage.
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

    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        lcs=self.lcs(word1,word2,m,n)
        l=len(lcs)
        return abs(l-m)+abs(l-n)