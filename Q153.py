## N
## Idea, approach and time complexity:
'''
The given code uses a modified binary search to find the minimum element in a rotated sorted array. It maintains two pointers, `l` (low) and `h` (high), and repeatedly 
narrows down the search range by comparing the middle element with the high element. If the middle element is greater than the high element, the minimum must be in the 
right half; otherwise, it’s in the left half. The time complexity of this approach is \(O(\log n)\) due to the halving of the search space in each iteration.
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,h=0,(len(nums)-1)
        while(l<h):
            m=(l+h)//2
            if(nums[m]>nums[h]):
                l=m+1
            else:
                h=m
        return nums[l]