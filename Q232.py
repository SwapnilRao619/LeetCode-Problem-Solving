## N
## Idea, approach and time complexity:
'''
The `MyQueue` class implements a queue using a list. Elements are added to the end with `push`, and removed from the front with `pop`. The `peek` method retrieves the 
front element without removing it, and `empty` checks if the queue is empty. The time complexity for `push` is O(1), while `pop` and `peek` are O(n) due to list removal 
sand access operations. To improve efficiency, a deque or two stacks could be used instead.
'''

class MyQueue:

    def __init__(self):
       self.s=[] 

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        p=self.s[0]
        self.s.remove(self.s[0])
        return p

    def peek(self) -> int:
        return self.s[0]

    def empty(self) -> bool:
        return len(self.s)==0
