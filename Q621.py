## N
## Idea, approach and time complexity:
'''
The problem is about scheduling tasks with a cooldown period, and the goal is to determine the least time to complete all tasks. The approach uses a max-heap to store the 
task frequencies and a queue to manage tasks that are cooling down. At each step, the most frequent task is selected, and it’s re-added to the queue with an updated 
cooldown. The process continues until all tasks are completed. Time complexity is O(T * log A), where T is the number of tasks and A is the number of distinct task types. 
This is because each task can be pushed and popped from the heap, and each task can be processed at most once.
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm={}
        gt=0
        q=deque()
        for i in tasks:
            hm[i]=hm.get(i,0)+1
        mh=[-val for val in hm.values()]
        heapq.heapify(mh)
        while(q or mh):
            gt+=1
            if(mh):
                num=1+heapq.heappop(mh)
                if(num!=0):
                    q.append([num,gt+n]) 
            if(q and q[0][1]==gt):
                heapq.heappush(mh,q.popleft()[0])
        return gt