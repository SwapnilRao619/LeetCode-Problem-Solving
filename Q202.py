## N
## Idea, approach and time complexity:
'''
The solution checks if a number is "happy" by repeatedly summing the squares of its digits. It tracks seen numbers to detect cycles. If it reaches 1, the number is happy; 
otherwise, it's not. The time complexity is primarily determined by the number of digits in `n` and the number of iterations before a cycle is detected or the number 
reaches 1. In the worst case, the time complexity is O(log n) for each iteration (due to the number of digits in `n`), and the number of iterations is bounded by a 
constant (since the sum of squares of digits quickly reduces large numbers to smaller values). Thus, the overall time complexity is O(log n).
'''

class Solution:
    def summer(self,n):
        sum=0
        while(n>0):
            sum+=(n%10)**2
            n//=10
        return sum
    def isHappy(self, n: int) -> bool:
        seen=set()
        while(n not in seen and n!=1):
            seen.add(n)
            n=self.summer(n)
        return n==1