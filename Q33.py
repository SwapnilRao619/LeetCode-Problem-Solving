## N
## Idea, approach and time complexity:
'''
The solution is designed to search for a target in a rotated sorted array. First, it finds the index of the smallest element (pivot) using binary search. Then, it 
performs binary search on the appropriate half of the array, based on whether the target is in the rotated portion or the sorted portion. The time complexity is 
\( O(\log n) \) because each binary search operation runs in logarithmic time.
'''

class Solution:
    def binSearch(self,arr,l,h,key):
        while(l<=h):
            m=(l+h)//2
            if(key<arr[m]):
                h=m-1
            elif(key>arr[m]):
                l=m+1
            else:
                return m
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l,h=0,(len(nums)-1)
        while(l<h):
            m=(l+h)//2
            if(nums[m]>nums[h]):
                l=m+1
            else:
                h=m
        smallpivot=l
        if(nums[smallpivot]<=target<=nums[-1]):
            return self.binSearch(nums,smallpivot,(len(nums)-1),target)
        else:
            return self.binSearch(nums,0,(smallpivot-1),target)
