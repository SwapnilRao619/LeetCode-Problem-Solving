## N
## Idea, approach and time complexity:
'''
The provided code implements a binary search algorithm to find the index of a target value in a sorted list of integers. It initializes two pointers, `l` and `r`, to 
represent the search boundaries and repeatedly calculates the midpoint `m`. Depending on the comparison between the target and the midpoint value, it adjusts the search 
range until the target is found or the range is exhausted. The time complexity of this algorithm is O(log n), making it efficient for large datasets.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,(len(nums)-1)
        while(l<=r):
            m=(l+r)//2
            if(nums[m]<target):
                l=m+1
            elif(nums[m]>target):
                r=m-1
            else:
                return m
        return -1
