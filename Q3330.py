## N
## Idea, approach and time complexity:
'''
The function `possibleStringCount` counts the number of contiguous segments of identical characters in the input string `word`. It initializes a counter and iterates 
through the string, incrementing the counter each time it encounters a character that is the same as the previous one. The time complexity of this approach is O(n), 
where n is the length of the string, as it processes each character exactly once.
'''

class Solution:
    def possibleStringCount(self, word: str) -> int:
        c=1
        for i in range(1,len(word)):
            if(word[i-1]==word[i]):
                c+=1
        return c
