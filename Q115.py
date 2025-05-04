## N
## Idea, approach and time complexity:
'''
The given solution calculates the number of distinct subsequences of string `s` that equal string `t` using dynamic programming. It constructs a 2D DP table `t` where 
`t[i][j]` represents the number of ways the first `j` characters of `t` can be formed using the first `i` characters of `s`. The base case initializes the first column 
as 1 since an empty `t` can be formed from any prefix of `s` by deleting all characters. For each character in `s` and `t`, if they match, the DP value is the sum of the 
values by including or excluding the current character of `s`; otherwise, it's just the value from excluding the character. This approach ensures that all subsequences 
are considered. The time and space complexity of the solution are both **O(m × n)**, where `m` is the length of `s` and `n` is the length of `t`.
'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s1,s2,m,n=s,t,len(s),len(t)
        t=[[0 for _ in range(n+1)] for _ in range(m+1)]
        t[0][0]=1
        for a in range(m+1):
            t[a][0]=1
        for a in range(1,m+1):
            for b in range(1,n+1):
                if(s1[a-1]==s2[b-1]):
                    t[a][b]=t[a-1][b-1]+t[a-1][b]
                else:
                    t[a][b]=t[a-1][b]
        return t[m][n]