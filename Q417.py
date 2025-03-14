## N
## Idea, approach and time complexity:
'''
The solution to the Pacific Atlantic Water Flow problem involves performing breadth-first search (BFS) starting from the boundaries of the Pacific and Atlantic oceans, 
respectively. The idea is to simulate how water flows from these oceans, ensuring it can only flow to adjacent cells with equal or higher heights. Two BFS queues are 
initialized: one for the Pacific (starting from the top and left edges of the grid) and one for the Atlantic (starting from the bottom and right edges). As the BFS 
explores, it marks all reachable coordinates for both oceans. Finally, the solution finds the intersection of the two sets of coordinates, which gives the cells that can 
flow to both oceans. The time complexity of the algorithm is O(m * n), where m and n are the dimensions of the grid, since each cell is processed once by both BFS 
searches. The space complexity is also O(m * n) due to the storage of visited cells and the queues used in BFS.
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        poq,pos=deque(),set()
        aoq,aos=deque(),set()
        m,n=len(heights),len(heights[0])
        for i in range(n):
            poq.append((0,i))
            pos.add((0,i))
        for i in range(1,m):
            poq.append((i,0))
            pos.add((i,0))
        for j in range(m):
            aoq.append((j,n-1))
            aos.add((j,n-1))
        for j in range(n-1):
            aoq.append((m-1,j))
            aos.add((m-1,j))
        def bfs(q,s):
            returnset=set()
            while(q):
                i,j=q.popleft()
                returnset.add((i,j))
                for x,y in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                    if(0<=x<m and 0<=y<n and heights[x][y]>=heights[i][j] and (x,y) not in s):
                        s.add((x,y))
                        q.append((x,y))
            return returnset
        aocoords=bfs(aoq,aos)
        pocoords=bfs(poq,pos)
        return list(aocoords.intersection(pocoords))