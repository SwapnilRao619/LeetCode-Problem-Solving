## N
## Idea, approach and time complexity:
'''
The provided code implements the Merge Sort algorithm, which sorts an array by recursively dividing it into halves (in the `halfer` method) until single-element arrays 
are reached. The `merger` method then combines these sorted halves back together. The overall time complexity of this approach is O(n log n), where n is the number of 
elements in the array, due to the logarithmic depth of the recursion and the linear time, needed to merge the sorted subarrays.
'''

class Solution:
    def merger(self,nums,l,m,r):
        left,right=nums[l:m+1],nums[m+1:r+1]
        i,j,k=l,0,0
        while(j<len(left) and k<len(right)):
            if(left[j]<right[k]):
                nums[l]=left[j]
                j+=1
            else:
                nums[l]=right[k]
                k+=1
            l+=1
        while(j<len(left)):
            nums[l]=left[j]
            j+=1
            l+=1
        while(k<len(right)):
            nums[l]=right[k]
            k+=1
            l+=1

    def halfer(self,nums,l,r):
        if(l==r):
            return
        m=(l+r)//2
        self.halfer(nums,l,m)
        self.halfer(nums,m+1,r)
        self.merger(nums,l,m,r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.halfer(nums,0,(len(nums)-1))
        return nums
