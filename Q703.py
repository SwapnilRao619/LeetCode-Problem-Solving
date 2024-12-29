## N
## Idea, approach and time complexity:
'''
The `KthLargest` class uses a min-heap to efficiently maintain the k largest elements from a list. In the constructor (`__init__`), the heap is initialized with the given 
list, and elements are popped until only k elements remain. The `add` method adds a new value to the heap, then ensures that the heap contains no more than k elements by 
popping the smallest element if necessary. The time complexity of both the initialization and the `add` method is O(n log k), where n is the number of elements in the 
list and k is the size of the heap. Each heap operation (push and pop) takes O(log k) time.
'''

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        self.k=k
        heapq.heapify(self.nums)
        while(len(self.nums)>self.k):
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        while(len(self.nums)>self.k):
            heapq.heappop(self.nums)
        return self.nums[0]