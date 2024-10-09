## N
## Idea, approach and time complexity:
'''
The provided code defines a function `removeElement` that modifies a list `nums` in-place to remove all instances of a specified value `val`. The approach uses a 
two-pointer technique: one pointer (`l`) tracks the position to place non-`val` elements, while the other (`r`) iterates through the list. If an element is not equal 
to `val`, it's moved to the `l` index, and `l` is incremented. The function returns the new length of the modified list. The time complexity of this solution is O(n), 
where n is the length of `nums`, since it involves a single pass through the list.
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        for r in nums:
            if r!=val:
                nums[l]=r
                l+=1
            else:
                continue
        return l