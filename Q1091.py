## N
## Idea, approach and time complexity:
'''
The approach used in this code is based on BFS, which is ideal for finding the shortest path in an unweighted grid. The algorithm starts by checking if the start or end 
cell is blocked (either grid[0][0] or grid[n-1][n-1] is 1), returning `-1` if so. Then, it initializes a queue with the starting position `(0, 0)` and a distance of 1. 
It iteratively explores all 8 possible directions from the current cell (up, down, left, right, and diagonals), ensuring each neighboring cell is within bounds and 
unvisited (represented by a 0 in the grid). If a valid neighboring cell is found, it is marked as visited (set to 1), and its position along with an incremented distance 
is added to the queue. The search continues until the bottom-right corner is reached, at which point the distance is returned. If the queue is exhausted without reaching 
the end, it returns `-1`. The time complexity of this algorithm is **O(n^2)**, where `n` is the size of the grid, since each cell is visited at most once, and we perform 
a constant amount of work for each cell.
'''

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if(grid[0][0] or grid[n-1][n-1]):
            return -1
        q=[(0,0,1)]
        grid[0][0]=1
        for i,j,d in q:
            if(i==n-1 and j==n-1):
                return d
            dir=[(i,j+1),(i+1,j),(i,j-1),(i-1,j),(i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)]
            for x,y in dir:
                if(0<=x<n and 0<=y<n and grid[x][y]==0):
                    grid[x][y]=1
                    q.append((x,y,d+1))
        return -1