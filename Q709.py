## N
## Idea, approach and time complexity:
'''
The function `toLowerCase` iterates through each character of the input string `s`, checks if it's uppercase, and converts it to lowercase if so. The approach involves 
concatenating the modified characters into a new string. The time complexity is O(n), where n is the length of the input string, as it processes each character exactly 
once.
'''

class Solution:
    def toLowerCase(self, s: str) -> str:
        ns=""
        for i in range(len(s)):
            if(s[i].isupper()):
                ns+=s[i].lower()
            else:
                ns+=s[i]
        return ns