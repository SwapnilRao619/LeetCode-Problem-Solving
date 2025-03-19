## N
## Idea, approach and time complexity:
'''
The solution to the problem of calculating the perimeter of an island in a 2D grid uses a straightforward approach by iterating through each cell in the grid. The idea is 
to treat each land cell (denoted by 1) as contributing 4 units to the perimeter. For each land cell, we then check its adjacent cells (top, bottom, left, right), and if 
any of these are also land cells (value 1), we subtract 1 from the perimeter for each adjacent land cell, as the shared edge does not contribute to the perimeter.The time 
complexity of this solution is O(m * n), where `m` is the number of rows and `n` is the number of columns in the grid, because each cell in the grid is visited once. The 
space complexity is O(1), as the solution only uses a constant amount of extra space beyond the input grid.
'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter=0
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    perimeter+=4
                    for x,y in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                        if(0<=x<m and 0<=y<n and grid[x][y]==1):
                            perimeter-=1
        return perimeter