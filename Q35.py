## Idea, approach and time complexity:
'''The code implements a binary search algorithm to find the insertion position of the target element in the sorted array nums in the searchInsert method. It 
initializes two pointers l and r to 0 and len(nums) - 1, respectively. Then, it iteratively updates the middle pointer m and compares the target with the element at 
index m. If the target is greater than the element at index m, it adjusts the l pointer to m + 1. If the target is less than the element at index m, it adjusts the r 
pointer to m - 1. Otherwise, it returns m. If not, then then l is returned as the index to insert the element to maintain the sorted property. The loop continues until 
l exceeds r. Overall, the approach efficiently finds the insertion position of the target element in the sorted array nums using binary search, achieving a time 
complexity of O(log n), where n is the length of the nums list.'''

## Code:
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while(l<=r):
            m=(l+r)//2
            if target>nums[m]:
                l=m+1
            elif target<nums[m]:
                r=m-1
            else: 
                return m
        return l