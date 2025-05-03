## N1
## Idea, approach and time complexity:
'''
The goal is to check if string s is a subsequence of string t. The code uses two pointers: i for s and j for t. It iterates through t, advancing i only when characters 
at s[i] and t[j] match. If i reaches the end of s, all characters of s were found in order in t. O(n), where n is the length of string t, since it makes a single pass 
through t.
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        while(j<len(t) and i<len(s)):
            if(s[i]==t[j]):
                i+=1
            j+=1
        return i==len(s)
    
## N2
## Idea, approach and time complexity:
'''
The given solution checks whether string `s` is a subsequence of string `t` using a dynamic programming approach based on computing the **Longest Common Subsequence 
(LCS)**. The `lcs` method constructs a 2D table `t` where each cell stores the LCS of prefixes of `s` and `t` up to that point. It fills the table by comparing 
characters of both strings: if they match, it appends the character to the LCS of the previous prefixes; if not, it takes the longer LCS from either the previous row or 
column. Finally, it checks if the computed LCS equals `s`. If so, `s` is a subsequence of `t`. The time and space complexity of this approach is **O(m × n)**, where `m` 
and `n` are the lengths of `s` and `t` respectively. This method is more computationally intensive than a simple two-pointer subsequence check but guarantees correctness.

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

    def isSubsequence(self, s: str, t: str) -> bool:
        m,n=len(s),len(t)
        lcs=self.lcs(s,t,m,n)
        return lcs==s