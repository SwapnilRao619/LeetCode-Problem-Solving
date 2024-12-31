## N
## Idea, approach and time complexity:
'''
The problem requires finding the maximum wealth of a customer, where wealth is the sum of values in each customer's account. The approach is to iterate through each 
customer's account, calculate the sum of the account balances, and update the maximum sum encountered. The time complexity is **O(m * n)**, where `m` is the number of 
customers and `n` is the number of accounts per customer, as we need to sum up all the elements in each customer's list.
'''

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ms=0
        for a in accounts:
            s=sum(a)
            if(s>ms):
                ms=s
        return ms