## N
## Idea, approach and time complexity:
'''
This solution finds the **longest palindromic substring** in a given string `s` by leveraging the concept of **Longest Common Substring (LCS)** between `s` and its 
reverse `s[::-1]`. It builds a dynamic programming (DP) table `t`, where `t[i][j]` stores the longest common substring ending at `s1[i-1]` and `s2[j-1]`. While filling 
this table, it only considers substrings that are also palindromes (checked via `ispalin`). The longest valid palindromic substring found during this process is returned. 
Although this approach cleverly combines LCS and palindrome checking, it is not the most efficient. The **time complexity** is **O(n²)** for filling the DP table and 
**O(n)** for each palindrome check (in the worst case), resulting in an overall complexity of **O(n³)**.
'''

class Solution:
    def ispalin(self,s):
        return s==s[::-1]

    def lcst(self,s1,s2,m,n):
        maxst=""
        t=[["" for _ in range(n+1)] for _ in range(m+1)]
        for a in range(1,m+1):
            for b in range(1,n+1):
                if(s1[a-1]==s2[b-1]):
                    t[a][b]=t[a-1][b-1]+s1[a-1]
                    if(len(maxst)<len(t[a][b]) and self.ispalin(t[a][b])):
                        maxst=t[a][b]
                else:
                    t[a][b]=""
        return maxst

    def longestPalindrome(self, s: str) -> str:
        s1,s2,m,n=s,s[::-1],len(s),len(s)
        lpst=self.lcst(s1,s2,m,n)
        return lpst