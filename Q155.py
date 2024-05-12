## Idea, approach and time complexity:
'''This code implements a stack with a getMin() function that retrieves the minimum element in constant time. It maintains two separate stacks: one for storing elements 
and the other for keeping track of minimum values. When pushing a value onto the stack, it updates the minimum stack accordingly. Popping an element updates both stacks, 
and getMin() returns the top element of the minimum stack, representing the current minimum value. All operations have a time complexity of O(1).'''

## Code:
class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif self.minstack[-1]<val:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]