## N
## Idea, approach and time complexity:
'''
The problem is solved using a binary search approach to find the single non-duplicate element in a sorted array. The key observation is that, in a properly paired array, 
the duplicates will always appear in even indices if the single element is on the left side, or in odd indices if it's on the right side. By checking the relationship 
between middle and adjacent elements, the search space is halved in each step. The time complexity is O(log n) due to the binary search.
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,h=0,(len(nums)-1)
        while(l<h):
            m=(l+h)//2
            if(m%2==0):
                if(nums[m]!=nums[m+1]):
                    h=m
                else:
                    l=m+2
            else:
                if(nums[m]!=nums[m+1]):
                    l=m+1
                else:
                    h=m
        return nums[l]