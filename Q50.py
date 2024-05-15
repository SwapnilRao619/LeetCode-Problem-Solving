## Idea, approach and time complexity:
'''The code implements a recursive approach to calculate the power of a given number x raised to an integer exponent n, breaking down the exponent into smaller parts 
(2^8 as 2^4X2^4 and 2^9 as 2X(2^4X2^4) so on) and recursively calculating the result. The time complexity of this solution is O(log n), making it efficient for large 
exponents.'''

## Code:
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def help(x,n):
            if x==0: return 0
            if n==0: return 1
            res=help(x,n//2)
            res=res*res
            return x*res if n%2 else res
        res=help(x,abs(n))
        return res if n>0 else 1/res