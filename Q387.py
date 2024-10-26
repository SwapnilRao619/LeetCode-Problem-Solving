## N
## Idea, approach and time complexity:
'''
The given code defines a method to find the index of the first non-repeating character in a string. It uses a dictionary to count occurrences of each character, marking 
non-repeating characters with a value of 0. After counting, it checks for the first character with this count and returns its index. The time complexity is O(n), where 
n is the length of the string, due to the two passes over the string: one for counting and another for finding the unique character.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm={}
        for i in range(len(s)):
            if(s[i] in hm):
                hm[s[i]]+=1
            else:
                hm[s[i]]=0
        for k,v in hm.items():
            if(v==0):
                return s.find(k)
        return -1