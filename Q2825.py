## N
## Idea, approach and time complexity:
'''
The approach uses a two-pointer technique to check if `str2` can be formed as a subsequence of `str1`, where each character in `str2` can either be the same as or the 
next character (cyclically, in the alphabet) from the corresponding character in `str1`. The pointers `i` and `j` iterate over `str1` and `str2` respectively. For each 
character in `str2`, it checks if the difference in their ASCII values is either 0 or 1 modulo 26, ensuring that the sequence can form a valid subsequence. The time 
complexity is O(m), where m is the length of `str1`, as we only traverse `str1` once.
'''

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i,j=0,0
        m,n=len(str1),len(str2)
        while(i<m and j<n):
            diff=(ord(str2[j])-(ord(str1[i])))%26
            if(diff==0 or diff==1):
                j+=1
            i+=1
        return j==n