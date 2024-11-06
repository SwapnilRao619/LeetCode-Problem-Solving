## N
## Idea, approach and time complexity:
'''
The `canSortArray` function attempts to sort an array `nums` using a modified insertion sort approach. It iterates over the list and performs swaps between adjacent 
elements if the elements have the same number of 1-bits in their binary representation and are out of order. The array is sorted in-place by repeatedly shifting 
elements until the condition is satisfied. Finally, the function checks if the array matches the fully sorted version. The time complexity of this approach is 
\(O(n^2)\), as the algorithm uses a nested loop similar to traditional insertion sort.
'''

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        ref=nums
        for i in range(len(nums)):
            j=i-1
            while(j>=0 and nums[j]>nums[j+1] and bin(nums[j]).count("1")==bin(nums[j+1]).count("1")):
                nums[j],nums[j+1]=nums[j+1],nums[j]
                j-=1
        return nums==sorted(ref)