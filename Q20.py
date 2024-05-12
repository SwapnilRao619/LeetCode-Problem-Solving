## Idea, approach and time complexity:
'''This code validates the correctness of brackets in a string using a stack. It iterates through the string, pushing opening brackets onto the stack and popping their 
corresponding closing brackets if encountered. Any mismatch or an empty stack with a closing bracket returns False. If the stack is empty at the end, it returns True. 
The time complexity is O(n), where n is the length of the input string.'''

## Code:
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hm={")":"(","}":"{","]":"["}
        for p in s:
            if p in hm.values():
                stack.append(p)
            elif stack and hm[p]==stack[-1]:
                stack.pop()
            else:
                return False
        return stack==[] #for cases like '(' as the p, checked if its an empty stack or not