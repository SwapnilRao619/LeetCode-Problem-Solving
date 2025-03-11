## N
## Idea, approach and time complexity:
'''
The solution uses a Breadth-First Search (BFS) to simulate the process of rotting oranges. Fresh oranges (1) are tracked in a set, and rotten oranges (2) are added to a 
queue. The BFS spreads the rot from adjacent rotten oranges to fresh ones, updating the grid and counting the time (in minutes) it takes for all fresh oranges to rot. If 
all fresh oranges rot, the number of minutes is returned. If some fresh oranges remain unrotted, `-1` is returned. The approach ensures all oranges are processed in the 
worst-case scenario, where each cell is visited once. The time complexity is **O(m * n)**, where `m` is the number of rows and `n` is the number of columns, as every cell 
is processed once.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=set()
        rotten=deque()
        m=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rotten.append((i,j))
                if(grid[i][j]==1):
                    fresh.add((i,j))
        while(fresh and rotten):
            m+=1
            for k in range(len(rotten)):
                r,c=rotten.popleft()
                for dir in [(r,c+1),(r+1,c),(r,c-1),(r-1,c)]:
                    if(dir in fresh):
                        fresh.remove(dir)
                        rotten.append(dir)
        return -1 if fresh else m