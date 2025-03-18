## N
## Idea, approach and time complexity:
'''
The given solution solves the flood fill problem using a breadth-first search (BFS) approach. The idea is to start from the given pixel `(sr, sc)` and change its color to 
the desired color if it matches the original color. A queue (`q`) is used to explore all connected pixels that share the same original color, ensuring that we only fill 
pixels within the same region. Each pixel is processed once, and neighboring pixels are added to the queue for further exploration. A set `seen` is used to track the 
pixels that have already been visited to avoid redundant work. The solution terminates once all connected pixels are filled with the new color. The time complexity of 
this algorithm is O(m * n), where `m` is the number of rows and `n` is the number of columns in the image, as in the worst case, all pixels need to be visited. The space 
complexity is also O(m * n) due to the space used by the queue and the `seen` set.
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if(color==image[sr][sc]):
            return image
        m,n=len(image),len(image[0])
        seen=set()
        q=deque()
        q.append((sr,sc))
        t=image[sr][sc]
        while(q):
            i,j=q.popleft()
            seen.add((i,j))
            image[sr][sc]=color
            for x,y in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                if(0<=x<m and 0<=y<n and image[x][y]==t and (x,y) not in seen):
                    image[x][y]=color
                    seen.add((x,y))
                    q.append((x,y))
        return image