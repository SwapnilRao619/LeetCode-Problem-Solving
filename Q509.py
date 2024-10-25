## N
## Idea, approach and time complexity:
'''
The provided code implements a recursive solution to compute the nth Fibonacci number, where the Fibonacci sequence is defined as \( F(n) = F(n-1) + F(n-2) \) with base 
cases \( F(0) = 0 \) and \( F(1) = 1 \). The approach relies on direct recursion, which can lead to repeated calculations for the same Fibonacci values. The time 
complexity is exponential, specifically \( O(2^n) \), due to the branching nature of the recursive calls, making it inefficient for larger values of \( n \).
'''

class Solution:
    def fib(self, n: int) -> int:
        if(n<=1):
            return n
        else:
            return (self.fib(n-1)+self.fib(n-2))