## N
## Idea, approach and time complexity:
'''
The function `sumOfMultiples` computes the sum of all integers from 1 to \( n \) that are multiples of 3, 5, or 7. It iterates through each number, checking if it's 
divisible by any of the specified factors and accumulates qualifying numbers in a list before returning their sum. The approach has a time complexity of \( O(n) \) due 
to the single loop through numbers up to \( n \).
'''

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans=[]
        for i in range(1,n+1):
            if(i%3==0 or i%5==0 or i%7==0):
                ans.append(i)
        return sum(ans)