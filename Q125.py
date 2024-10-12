## N
## Idea, approach and time complexity:
'''
The problem asks whether a given string is a palindrome, considering only alphanumeric characters and ignoring cases. The approach involves filtering the string to 
retain only alphanumeric characters, converting them to lowercase, and then checking if the resulting string reads the same forwards and backwards using a two-pointer 
technique. The time complexity of this solution is O(n), where n is the length of the input string, due to the linear scans for filtering and comparing characters.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence=''.join(c.lower() for c in s if c.isalnum())
        l,r=0,(len(sentence)-1)
        while(l<r):
            if(sentence[l]==sentence[r]):
                l+=1
                r-=1
            else:
                return False
        return True