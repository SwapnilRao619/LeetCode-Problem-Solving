## N
## Idea, approach and time complexity:
'''
The method removes duplicates from a sorted list `nums` in place by using two pointers: `l` for the position of unique elements and `r` for iterating through the list. 
When a new unique element is found (i.e., `nums[r]` is different from `nums[r-1]`), it’s placed at `nums[l]`, and `l` is incremented. The process continues until the 
end of the list, and the method returns the count of unique elements. The time complexity is O(n), as it makes a single pass through the list.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1
        return l