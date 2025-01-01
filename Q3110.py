class Solution:
    def scoreOfString(self, s: str) -> int:
        sc=0
        for i in range(len(s)-1):
            sc+=(abs(ord(s[i])-ord(s[i+1])))
        return sc
