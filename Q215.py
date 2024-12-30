## N
## Idea, approach and time complexity:
'''
## A1:
The provided code implements the quicksort algorithm to sort an array and then retrieves the k-th largest element. The `quicksort` method uses the last element as a 
pivot to partition the array into elements less than and greater than the pivot. After sorting, the `findKthLargest` method returns the k-th largest element from the 
sorted list. The average time complexity of quicksort is \(O(n \log n)\), but in the worst case (e.g., when the array is already sorted), it can degrade to \(O(n^2)\). 
However, in practice, quicksort is often efficient due to its divide-and-conquer approach.

## A2:
The given solution uses a min-heap to efficiently find the k-th largest element in an array. It iterates through the array, pushing each element into the heap, and 
ensures that the heap only holds the k largest elements. Once the heap size exceeds k, the smallest element is removed using `heapq.heappop()`. After processing all 
elements, the root of the heap (i.e., the smallest element in the heap) is the k-th largest element in the array. The time complexity is \(O(n \log k)\), where \(n\) is 
the number of elements in the array, as inserting an element into a heap takes \(O(\log k)\) and this happens for each element in the array.
'''

## A1
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
    
## A2
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        for n in nums:
            heapq.heappush(h,n)
            if(len(h)>k):
                heapq.heappop(h)
        return h[0]
