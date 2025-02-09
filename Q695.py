## N
## Idea, approach and time complexity:
'''
The problem is to find the maximum area of an island in a 2D grid, where 1 represents land and 0 represents water. The approach uses Depth-First Search (DFS) to explore 
all connected lands starting from each unvisited land cell. For each island, we count the number of connected land cells (the area) and keep track of the maximum area 
found. The time complexity is O(r * c), where `r` and `c` are the number of rows and columns in the grid, because each cell is visited once.
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        maxar=0
        def dfs(i,j):
            if(i<0 or i>=r or j<0 or j>=c or grid[i][j]==0):
                return 0
            grid[i][j]=0
            return 1+dfs(i,j+1)+dfs(i+1,j)+dfs(i,j-1)+dfs(i-1,j)
        for i in range(r):
            for j in range(c):
                if(grid[i][j]==1):
                    maxar=max(maxar,dfs(i,j))
        return maxar
