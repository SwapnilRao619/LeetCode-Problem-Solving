## N
## Idea, approach and time complexity:
'''
The provided code rearranges a list of integers by first sorting it and then swapping every pair of adjacent elements. The approach involves sorting the list, which has 
a time complexity of \(O(n \log n)\), followed by a linear pass to swap elements, resulting in an overall complexity of \(O(n \log n)\). This method efficiently creates 
a new arrangement while using constant space for swapping.
'''

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        i=0
        while(i<len(nums)):
            nums[i],nums[i+1]=nums[i+1],nums[i]
            i+=2
        return nums