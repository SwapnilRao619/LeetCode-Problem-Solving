## N 1
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
        
## N 2
## Idea, approach and time complexity:
'''
This solution uses **memoization** to optimize the Fibonacci calculation by storing previously computed values in a cache. The base cases are when `n` is 0 or 1, 
returning `n` directly. For other values, the function checks the cache for precomputed results, and if not found, it recursively computes `fib(n-1)` and `fib(n-2)`, 
storing the result. This approach reduces redundant computations, making the time complexity **O(n)**, as each Fibonacci number is computed only once and retrieved from 
the cache in constant time.
'''

class Solution:
    def __init__(self):
        self.cache={}
    def fib(self, n: int) -> int:
        if(n==1 or n==0):
            return n
        if(n in self.cache):
            return self.cache[n]
        self.cache[n]=self.fib(n-1)+self.fib(n-2)
        return self.cache[n]
