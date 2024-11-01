## N
## Idea, approach and time complexity:
'''
The function `makeFancyString` removes consecutive duplicate characters from the input string `s`, ensuring no character appears more than twice in a row. It constructs 
a new string starting with the first two characters and then adds characters from the rest of the string based on the condition that they differ from the previous two 
characters. The time complexity is O(n), where n is the length of the string, as it involves a single pass through the string to build the result.
'''

class Solution:
    def makeFancyString(self, s: str) -> str:
        if(len(s)<2):
            return s
        fs=s[0]+s[1]
        rsia=[s[i] for i in range(2,len(s)) if s[i]!=s[i-1] or s[i]!=s[i-2]]
        return fs+''.join(rsia)