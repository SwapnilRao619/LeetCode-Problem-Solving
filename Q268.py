## N
## Idea, approach and time complexity:
'''
The approach calculates the sum of numbers from 0 to `n` and subtracts the sum of elements in the input list `nums`. The difference reveals the missing number. The time 
complexity is O(n), where `n` is the length of `nums`, due to the summing operations.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return abs(sum(nums)-sum([x for x in range(len(nums)+1)]))