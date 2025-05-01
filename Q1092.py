## N
## Idea, approach and time complexity:
'''
The given code computes the **Shortest Common Supersequence (SCS)** of two strings `str1` and `str2` using **dynamic programming and the Longest Common Subsequence 
(LCS)**. The approach starts by computing the LCS of the two strings, which identifies the common subsequence that should be preserved in order. Then, it constructs the 
SCS by merging characters from both strings while maintaining the order of the LCS: it adds non-LCS characters from both strings as they appear and inserts LCS 
characters in sequence. This ensures that both input strings are subsequences of the result. The time complexity is **O(m * n)** for computing the LCS (where `m` and `n` 
are the lengths of `str1` and `str2`, respectively), and **O(m + n)** for building the final SCS from the LCS, making the overall time complexity **O(m * n)**.
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

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        lcs=self.lcs(str1,str2,len(str1),len(str2))
        i,j,res=0,0,[]
        for c in lcs: #for length, len(str1)+len(str2)-len(lcs)=len(scs)
            while(str1[i]!=c):
                res.append(str1[i])
                i+=1
            while(str2[j]!=c):
                res.append(str2[j])
                j+=1
            i,j=i+1,j+1
            res.append(c)
        res.append(str1[i:])
        res.append(str2[j:])
        return ''.join(res)