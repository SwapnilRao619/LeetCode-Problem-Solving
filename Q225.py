## Idea, approach and time complexity:
'''This code implements a stack using a Python list. It provides standard stack operations: push, pop, top, and empty. Elements are appended to the end of the list for 
push operations, simulating the stack's top. Pop removes and returns the top element, top returns the top element without removal, and empty checks if the stack is empty.
All operations have an average time complexity of O(1), except pop, which may take O(n) in the worst case due to list resizing.'''

## Code:
class MyStack:

    def __init__(self):
        self.q=[]

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        if self.q:
            v=self.q[-1]
            self.q.pop()
            return v

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q)==0