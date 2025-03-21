## N
## Idea, approach and time complexity:
'''
The solution uses a hash map to count the frequency of each character in the string. It first iterates through the string to populate the map, then checks for the first 
character with a count of 1. If found, its index is returned; otherwise, -1 is returned. The time complexity is O(n) because the string is traversed twice, and the space 
complexity is O(k), where k is the number of unique characters.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm={}
        for i in s:
            if(i not in hm):
                hm[i]=1
            else:
                hm[i]+=1
        for  i in range(len(s)):
            if(hm[s[i]]==1):
                return i
        return -1
