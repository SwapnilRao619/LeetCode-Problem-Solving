## N
## Idea, approach and time complexity:
'''
The given solution solves the problem of capturing "O" regions surrounded by "X" on a board by using a breadth-first search (BFS) approach. The idea is to first identify 
all the "O" regions that are connected to the borders of the board (since these "O"s cannot be captured). This is done by performing BFS starting from all "O"s that 
appear on the borders (first and last row, first and last column), marking all reachable "O"s as "T" (temporarily marked) during the BFS traversal. Once the BFS is 
complete, all the "O"s that are not marked as "T" (those not connected to the border) are surrounded by "X", as they are captured regions. Finally, all the temporarily 
marked "T"s are converted back to "O" to restore the regions that should not be captured. The time complexity of this approach is O(M * N), where M is the number of rows 
and N is the number of columns in the board. This is because we traverse every cell on the board once during the BFS and the final marking steps.
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def bfs(i,j):
            board[i][j]="T"
            q=deque()
            q.append((i,j))
            while(q):
                i,j=q.popleft()
                for dir in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                    x,y=dir
                    if(0<=x<len(board) and 0<=y<len(board[0]) and board[x][y]=="O"):
                        board[x][y]="T"
                        q.append((x,y))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if((i in [0,len(board)-1] or j in [0,len(board[0])-1]) and board[i][j]=="O"):
                    bfs(i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]=="O"):
                    board[i][j]="X"
                elif(board[i][j]=="T"):
                    board[i][j]="O"