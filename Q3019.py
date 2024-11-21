## N
## Idea, approach and time complexity:
'''
The given code counts the number of key changes in a string, where a "key change" occurs when the case (upper or lower) of a character differs from the previous 
character. The approach iterates through the string, comparing each character's case (using `lower()` to handle case-insensitivity) with the previous one. If they differ, 
it increments the count. The time complexity is O(n), where n is the length of the string, as it processes each character once.
'''

class Solution:
    def countKeyChanges(self, s: str) -> int:
        count=0
        lk=s[0]
        for i in range(len(s)):
            if(lk.lower()!=s[i].lower()):
                lk=s[i]
                count+=1
        return count