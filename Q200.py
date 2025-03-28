## N
## Idea, approach and time complexity:
'''
The approach used in this solution is Depth-First Search (DFS) to explore and mark all the connected lands in the grid as visited (by changing "1" to "0"). Starting from 
any land cell ("1"), the DFS recursively explores its neighboring cells (up, down, left, right) and marks the entire island as visited. The solution then counts the 
number of such DFS calls, representing the number of islands. The algorithm visits each cell once, making the time complexity O(r * c), where r is the number of rows and 
c is the number of columns in the grid.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r,c=len(grid),len(grid[0])
        def dfs(i,j):
            if(i<0 or i>=r or j<0 or j>=c or grid[i][j]!="1"):
                return
            else:
                grid[i][j]="0"
                dfs(i,j+1)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i-1,j)
        islands=0
        for i in range(r):
            for j in range(c):
                if(grid[i][j]=="1"):
                    islands+=1
                    dfs(i,j)
        return islands