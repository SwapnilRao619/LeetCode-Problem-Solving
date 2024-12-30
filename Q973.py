## N
## Idea, approach and time complexity:
'''
The solution uses a min-heap to efficiently find the k closest points to the origin. For each point in the list, the Euclidean distance from the origin is calculated and 
pushed into the heap along with the point itself. The heap is structured to maintain the smallest distances at the top. After processing all points, the algorithm pops 
the k smallest elements, returning the k closest points. The time complexity is \(O(n \log n)\), where \(n\) is the number of points. This is due to the heap operations 
(push and pop) for each of the \(n\) points, each of which takes \(O(\log n)\).
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        for p in points:
            heapq.heappush(h,[(p[0]**2+p[1]**2)**0.5,p])
        return [heapq.heappop(h)[1] for _ in range(k)]