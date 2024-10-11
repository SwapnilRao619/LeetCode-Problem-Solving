## N
## Idea, approach and time complexity:
'''
The code implements a solution to evaluate a series of score operations in a game, using a stack to manage scores. It processes each operation: adding a score, doubling 
the last score, summing the last two scores, or canceling the last score. The final score is calculated by summing all values in the stack. The time complexity is O(n), 
where n is the number of operations, as each operation is processed in constant time.
'''

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2*stack[-1])
            elif op =="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)