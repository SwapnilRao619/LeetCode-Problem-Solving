## N
## Idea, approach and time complexity:
'''
The function computes the sum of integers from 1 to `n` that are not divisible by `m` and the sum of those that are divisible by `m`, then returns the difference between 
the two sums. It iterates through all numbers from 1 to `n` to calculate these sums. The time complexity is O(n) due to the loop that processes each number once.
'''

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1=sum(i for i in range(1,(n+1)) if i%m!=0)
        num2=sum(i for i in range(1,(n+1)) if i%m==0)
        return num1-num2