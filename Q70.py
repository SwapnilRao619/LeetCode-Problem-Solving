## N
## Idea, approach and time complexity:
'''
The given solution uses an iterative approach to solve the "Climbing Stairs" problem, which is based on the Fibonacci sequence. It maintains two variables, `p1` and `p2`, 
representing the number of ways to reach the current and the previous step, respectively. The time complexity is O(n), as it iterates through the stairs once. The space 
complexity is O(1), since it uses only a fixed amount of extra space.
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        p1,p2=1,1
        for i in range(n-1):
             t=p1
             p1=p1+p2
             p2=t
        return p1