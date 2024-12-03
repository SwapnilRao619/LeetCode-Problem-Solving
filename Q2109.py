## N
## Idea, approach and time complexity:
'''
The problem requires inserting spaces into a given string `s` at specified positions in the list `spaces`. The approach involves iterating through the `spaces` list and 
using the indices to slice the string, appending each slice to a result string with a space at the appropriate locations. After processing all space positions, the 
remaining substring is appended. The time complexity is O(n + m), where `n` is the length of the string `s` and `m` is the number of spaces, as each character is 
processed once and the space insertions are linear.
'''

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        st=""
        k=0
        for i in range(len(spaces)):
            st+=s[k:spaces[i]]+" "
            k=spaces[i]
        st+=s[k:len(s)]
        return st