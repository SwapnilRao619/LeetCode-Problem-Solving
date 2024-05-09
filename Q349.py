## Idea, approach and time complexity:
'''The code implements an intersection algorithm to find the common elements between two arrays, nums1 and nums2. It first creates a hashset, hs, to store the unique 
elements of nums1. Then, it iterates through nums2 and checks if each element is present in the hashset. If the element is found, it is added to the result list, res, 
and removed from the hashset to ensure uniqueness. Finally, the function returns the list of common elements. The approach efficiently finds the intersection of two 
arrays using a hashset, achieving a time complexity of O(n), where n is the size of the larger array.'''

## Code:
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        hs=set(nums1) #the hashset stores unique elements
        for i in nums2:
            if i in hs:
                res.append(i)
                hs.remove(i)
        return res