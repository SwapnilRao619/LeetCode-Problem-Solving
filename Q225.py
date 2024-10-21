## N
## Idea, approach and time complexity:
'''
The `MyStack` class implements a stack using a deque to simulate stack operations. The `push` method adds elements to the back of the deque, while `pop` and `top` 
involve rotating the deque to access the last element efficiently. The `empty` method checks if the deque is empty. The time complexity for `push` is O(1), while `pop` 
and `top` have a time complexity of O(n) due to the need to rotate the elements.
'''

class MyStack:

    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q)==0
