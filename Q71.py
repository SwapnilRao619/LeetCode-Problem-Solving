## Idea, approach and time complexity:
'''The given code simplifies a Unix-style file path by splitting it into components and processing each component using a stack. It initializes an empty stack and 
splits the path string into components. It then iterates through each component, pushing valid directories onto the stack, and popping the last directory if 
encountering "..". It constructs the simplified path by joining the stack components with '/'. The time complexity is O(n), where n is the length of the input path 
string, due to splitting, filtering, and joining operations.'''

## Code:
class Solution:
    def simplifyPath(self, path: str) -> str:
        m=path.split('/')
        m=[i for i in m if i!=""]
        stack=[]
        for i in m:
            if i=="..":
                if stack: stack.pop()
            elif i==".":
                continue
            else:
                stack.append(i)
        return "/"+"/".join(stack) #'/' is the delimiter here to remove from the stack  