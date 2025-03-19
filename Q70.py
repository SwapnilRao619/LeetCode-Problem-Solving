## N 1
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
    
## N 2
## Idea, approach and time complexity:
'''
The given solution is a dynamic programming approach to solve the "Climbing Stairs" problem. The idea is to calculate the number of ways to reach the nth step by 
recognizing that the number of ways to reach step `n` is the sum of the ways to reach steps `n-1` and `n-2`. The solution uses memoization to store previously computed 
results in a cache (`self.cache`) to avoid redundant calculations, improving efficiency. The base cases are when `n` is 1 or 2, where there are directly 1 or 2 ways to 
reach the top. By using memoization, the time complexity is reduced to **O(n)**, where `n` is the number of steps, since each value is calculated only once and stored for 
future use.
'''

class Solution:
    def __init__(self):
        self.cache={}
    def climbStairs(self, n: int) -> int:
        if(n==1 or n==2):
            return n
        if(n in self.cache):
            return self.cache[n]
        self.cache[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.cache[n]
