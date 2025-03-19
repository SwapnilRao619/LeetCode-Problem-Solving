## N
## Idea, approach and time complexity:
'''
The function checks if a given string of parentheses is valid by using a stack. It iterates through the string, pushing opening brackets onto the stack and popping them 
when a matching closing bracket is encountered. If a closing bracket doesn't match the top of the stack or the stack is empty when it shouldn't be, the function returns 
`False`. Finally, it checks if the stack is empty to confirm all brackets were matched correctly. The time complexity is **O(n)**, where **n** is the length of the 
string, as each character is processed once.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hm={')':'(','}':'{',']':'['}
        for p in s:
            if(p=='(' or p=='{' or p=='['):
                stack.append(p)
            elif(p==')' or p=='}' or p==']'):
                if(stack and stack[-1]==hm[p]):
                    stack.pop()
                else:
                    return False
        return len(stack)==0
