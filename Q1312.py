## N
## Idea, approach and time complexity:
'''
The given solution aims to find the **minimum number of insertions required to make a string a palindrome**. The key idea is based on computing the LPS of the string `s`, 
which is equivalent to finding the **Longest Common Subsequence (LCS)** between the string and its reverse (`s[::-1]`). Once the LPS is known, the minimum insertions 
needed will be the difference between the original string length and the length of the LPS (`len(s) - len(lps)`). The approach uses dynamic programming to build an LCS 
table (`t`) of size `(m+1) x (n+1)` where `m` and `n` are the lengths of the two strings (both equal to `len(s)` in this case). The LCS is built by comparing characters 
and choosing either the previous best result or appending the matched character. **Time complexity is O(n²)** due to the nested loops over the string lengths, and 
**space complexity is also O(n²)** because of the 2D table used to store intermediate LCS strings.
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

    def minInsertions(self, s: str) -> int:
        s1,s2,m,n=s,s[::-1],len(s),len(s)
        lps=self.lcs(s1,s2,m,n)
        return abs(len(lps)-len(s))