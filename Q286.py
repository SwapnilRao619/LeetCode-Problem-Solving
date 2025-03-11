## N
## Idea, approach and time complexity:
'''
The problem at hand is to fill each empty room in a 2D grid with the distance to its nearest gate, where the gates are represented by 0, empty rooms by INF, and walls by 
a non-zero value. The solution employs a **Breadth-First Search (BFS)** approach, which is ideal for problems involving shortest path in an unweighted grid. The algorithm 
first identifies all the gates (cells with value 0) and enqueues their positions into a queue. It then performs BFS, where for each gate, it explores all neighboring 
cells (up, down, left, right) and updates their distance from the gate if they are unvisited (i.e., have value INF). This continues until all reachable rooms are filled 
with the shortest distance to a gate. The time complexity of this approach is **O(m * n)**, where `m` is the number of rows and `n` is the number of columns in the grid. 
This is because, in the worst case, every cell in the grid will be processed once. The space complexity is **O(m * n)** due to the queue storing the positions of the 
gates and rooms during the BFS traversal.
'''

from typing import (
    List,
)
from collections import (
    deque,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        m=len(rooms)
        n=len(rooms[0])
        INF=2**31-1
        q=deque()
        d=0
        for i in range(m):
            for j in range(n):
                if(rooms[i][j]==0):
                    q.append((i,j))
        while(q):
            d+=1
            for _ in range(len(q)):
                i,j=q.popleft()
                for dir in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                    x,y=dir
                    if(0<=x<m and 0<=y<n and rooms[x][y]==INF):
                        rooms[x][y]=d
                        q.append((x,y))
        return rooms