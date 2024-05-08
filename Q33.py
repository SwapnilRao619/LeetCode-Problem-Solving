## Idea, approach and time complexity:
'''The code implements a binary search algorithm to find the target element in the rotated sorted array. It first checks if the array has only one element and if it 
matches the target. Then, it initializes low and high pointers to the start and end of the array, respectively. The algorithm iteratively updates the mid pointer 
and compares the target with the elements at the mid index. If the target is found, it returns the index. Otherwise, it adjusts the low and high pointers based on 
the relative positions of the target and mid element, ensuring that the search space is reduced in each iteration. If the target is not found, the function returns 
-1. Overall, the approach is to efficiently search for the target element in a rotated sorted array using binary search, achieving O(log n) runtime complexity.'''

## Code:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]==target:
                return 0
        low=0;
        high=(len(nums))-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[low]:
                if target>=nums[low] and target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if target>nums[mid] and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1