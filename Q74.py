## Idea, approach and time complexity:
'''The code implements a binary search algorithm to search for the target element in a 2D matrix. It first determines the number of rows and columns in the matrix. 
Then, it initializes two pointers, top and bot, to represent the top and bottom rows of the matrix, respectively. The algorithm iteratively updates these pointers to 
narrow down the search space vertically based on the target value. Once it finds the row where the target might be located, it performs another binary search 
horizontally within that row. If the target is found in the row, the function returns True; otherwise, it returns False. The approach efficiently searches for the 
target element in the matrix using binary search, achieving O(log (n*m)) runtime complexity.'''

## Code:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix), len(matrix[0]) 
        top,bot=0,rows-1
        while(top<=bot):
            row=(top+bot)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bot=row-1
            else:
                break
        if not (top<=bot):
            return False
        row=(top+bot)//2
        l,r=0,cols-1
        while(l<=r):
            mid=(l+r)//2
            if target>matrix[row][mid]:
                l=mid+1
            elif target<matrix[row][mid]:
                r=mid-1
            else:
                return True
        return False