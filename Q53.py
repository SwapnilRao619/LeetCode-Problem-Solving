## N
## Idea, approach and time complexity:
'''
The provided solution implements Kadane's algorithm to solve the "Maximum Subarray Problem," which aims to find the contiguous subarray with the largest sum in a given 
list of integers. The algorithm works by iterating through the array and, for each element, checking if adding the previous element's value (if it's positive) results in 
a larger sum. If it does, the current element is updated by adding the previous element’s value, thus extending the current subarray. If the previous element is negative, 
it's better to start a new subarray with the current element. This process ensures that at each step, the sum of the best subarray ending at the current element is 
captured. The final result is obtained by returning the maximum value in the modified array, which represents the largest sum of any contiguous subarray. The time 
complexity of this solution is O(n), where n is the number of elements in the array. This is because the algorithm only requires a single traversal of the input array, 
performing constant-time operations at each step. The space complexity is O(1) as the solution modifies the array in place without using any extra data structures.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if(nums[i-1]>0):
                nums[i]+=nums[i-1]
        return max(nums)