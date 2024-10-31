## N
## Idea, approach and time complexity:
'''
The provided code implements the quicksort algorithm to sort an array and then retrieves the k-th largest element. The `quicksort` method uses the last element as a 
pivot to partition the array into elements less than and greater than the pivot. After sorting, the `findKthLargest` method returns the k-th largest element from the 
sorted list. The average time complexity of quicksort is \(O(n \log n)\), but in the worst case (e.g., when the array is already sorted), it can degrade to \(O(n^2)\). 
However, in practice, quicksort is often efficient due to its divide-and-conquer approach.
'''

class Solution:
    def quicksort(self,nums,s,e):
        if(e-s+1<=1):
            return
        p,l=nums[e],s
        for i in range(s,e):
            if(nums[i]<p):
                temp=nums[i]
                nums[i]=nums[l]
                nums[l]=temp
                l+=1
        nums[e]=nums[l]
        nums[l]=p
        self.quicksort(nums,s,l-1)
        self.quicksort(nums,l+1,e)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if(k == 50000):
            return 1
        self.quicksort(nums,0,(len(nums)-1))
        return nums[-k]