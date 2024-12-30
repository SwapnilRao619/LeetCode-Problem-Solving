## N
## Idea, approach and time complexity:
'''
The solution uses a max-heap to simulate the process of smashing stones. It first negates all stone weights to work with Python's `heapq`, which is a min-heap by default, 
and converts it to a max-heap. In each iteration, the two largest stones are popped, and if they are different, the result of their collision (difference) is pushed back 
into the heap. This continues until one or no stone remains. The time complexity is \(O(n \log n)\), where \(n\) is the number of stones, due to heap operations (push and 
pop) in each iteration.
'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while(len(stones)>1):
            y=heapq.heappop(stones)
            x=heapq.heappop(stones)
            if(y!=x):
                heapq.heappush(stones,y-x)
        return -heapq.heappop(stones) if stones else 0