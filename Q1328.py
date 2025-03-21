## N
## Idea, approach and time complexity:
'''
The problem is to break a palindrome string by changing one character to make it lexicographically smallest. The approach is to check if the string is of length 1. If so, 
return an empty string as it’s impossible to break it. For longer strings, the algorithm tries to replace the first non-'a' character with 'a' (since 'a' is the 
lexicographically smallest letter) to make the string not a palindrome. If this change doesn’t break the palindrome, the code then tries to change the last 'a' to 'b'. 
This ensures the smallest lexicographically valid change. The time complexity is O(n) because we scan the string twice (once from left to right and once from right to 
left), where n is the length of the string.
'''

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n=len(palindrome)
        if(n==1):
            return ""
        p=list(palindrome)
        for i in range(n):
            if(p[i]!="a"):
                p[i]="a"
                break
        if p!=p[::-1]: 
            return ''.join(p) 
        p=list(palindrome)
        for i in range(n-1,-1,-1):
            if(p[i]=="a"):
                p[i]="b"
                break
        return ''.join(p)