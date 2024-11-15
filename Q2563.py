## N
## Idea, approach and time complexity:
'''
The solution uses a two-pointer or binary search approach to count pairs of numbers from the sorted `nums` array whose sum falls within the given range [lower, upper]. 
For each element `nums[i]`, it calculates the lower and upper bounds (`x` and `y`) for the second number in the pair, then uses binary search (`bisect_left` and 
`bisect_right`) to find the range of valid pairs efficiently. The time complexity of this approach is O(n log n) due to sorting and binary searches for each element, 
where n is the size of the input array `nums`.
'''

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        allPairs=0
        nums=sorted(nums)
        for i in range(len(nums)-1):
            x=lower-nums[i]
            y=upper-nums[i]
            leftI=bisect_left(nums,x,i+1)
            rightI=bisect_right(nums,y,i+1)
            allPairs+=(abs(leftI-rightI))
        return allPairs