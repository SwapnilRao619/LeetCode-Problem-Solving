## N
## Idea, approach and time complexity:
'''
The idea behind this solution is to square each element in the input list `nums` and then return the list of squared values sorted in non-decreasing order. The approach 
involves iterating through the list, squaring each element, and appending it to a new list, followed by sorting the result. The time complexity is O(n log n) due to the 
sorting step, where `n` is the length of the input list. The squaring operation itself takes O(n).
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[i]*nums[i])
        return sorted(ans)