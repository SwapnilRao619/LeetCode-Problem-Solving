## N
## Idea, approach and time complexity:
'''
The provided code implements the Merge Sort algorithm, which is a divide-and-conquer sorting technique. The approach involves recursively splitting the input array `nums` 
into smaller subarrays until each subarray contains a single element, as a single element is inherently sorted. The `halfer` method handles this recursive splitting, 
while the `merge` method is responsible for merging the sorted subarrays back together in a sorted manner. During the merge process, two pointers are used to compare 
elements from the left and right subarrays, ensuring that the merged result remains sorted. The overall time complexity of the Merge Sort algorithm is O(n log n), where 
n is the number of elements in the input array. This efficiency arises from the logarithmic number of divisions (due to halving) and linear time spent merging the 
subarrays at each level of recursion. Merge Sort is particularly advantageous for large datasets and provides stable sorting, maintaining the relative order of equal 
elements.
'''

class Solution:
    def merge(self,nums,l,m,r):
        left,right=nums[l:m+1],nums[m+1:r+1]
        i,j,k=l,0,0
        while(j<len(left) and k<len(right)):
            if(left[j]<=right[k]):
                nums[i]=left[j]
                j+=1
            else:
                nums[i]=right[k]
                k+=1
            i+=1
        while(j<len(left)):
            nums[i]=left[j]
            j+=1
            i+=1
        while(k<len(right)):
            nums[i]=right[k]
            k+=1
            i+=1

    def halfer(self,nums,l,r):
        if(l==r):
            return nums
        m=(l+r)//2
        self.halfer(nums,l,m)
        self.halfer(nums,m+1,r)
        self.merge(nums,l,m,r)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1
        return self.halfer(nums,l,r)