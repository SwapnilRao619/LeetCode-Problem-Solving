## N
## Idea, approach and time complexity:
'''
The approach is to iterate through all integers from 1 to `n` and add them to the sum only if they are not in the `banned` set and if adding the number doesn't exceed the 
`maxSum`. The algorithm stops once adding another number would exceed the `maxSum`. The time complexity is **O(n)** because the loop iterates through all integers from 1 
to `n`, and each set lookup operation (`i not in banned`) takes **O(1)** on average.
'''

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned=set(banned)
        sumv,count=0,0
        for i in range(1,n+1):
            if(i not in banned and sumv+i<=maxSum):
                sumv+=i
                count+=1
        return count