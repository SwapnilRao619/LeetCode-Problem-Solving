## Idea, approach and time complexity:
'''This code implements a queue using a Python list. It supports push, pop, peek, and empty operations. Elements are added to the end of the list for push operations, 
simulating the rear of the queue. Pop removes and returns the first element, peek returns the first element without removal, and empty checks if the queue is empty. 
All operations have an average time complexity of O(1), except pop, which may take O(n) in the worst case due to list resizing.'''

## Code:
class MyQueue:

    def __init__(self):
        self.s=[]

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        if self.s:
            v=self.s[0]
            self.s.remove(self.s[0])
            return v

    def peek(self) -> int:
        return self.s[0]

    def empty(self) -> bool:
        return len(self.s)==0