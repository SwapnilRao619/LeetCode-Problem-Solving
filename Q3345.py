## N
## Idea, approach and time complexity:
'''
The solution finds the smallest number greater than or equal to `n` whose digit product is divisible by `t`. It iterates through numbers starting from `n`, calculating 
the product of their digits until it satisfies the condition. The time complexity is \(O(k \cdot d)\), where \(k\) is the number of iterations and \(d\) is the number 
of digits in each number.
'''

class Solution:
    def cdp(self,num):
        prod=1
        while(num>0):
            prod*=(num%10)
            num//=10
        return prod

    def smallestNumber(self, n: int, t: int) -> int:
        pn=n
        while(self.cdp(pn)%t!=0):
            pn+=1
        return pn