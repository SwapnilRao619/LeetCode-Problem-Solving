## N
## Idea, approach and time complexity:
'''
The approach of this solution uses a two-step binary search on a 2D matrix. First, it identifies the correct row that may contain the target by comparing the target with 
the first and last elements of each row. Once the potential row is found, a second binary search is performed within that row to find the target. This efficient method 
leverages the sorted nature of the matrix, resulting in a time complexity of \(O(\log m + \log n)\), where \(m\) is the number of rows and \(n\) is the number of columns 
in the matrix.
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t,b=0,(len(matrix)-1)
        while(t<=b):
            r=(t+b)//2
            if(matrix[r][-1]<target):
                t=r+1
            elif(matrix[r][0]>target):
                b=r-1
            else:
                break
        if(not t<=b):
            return False
        r=(t+b)//2
        l,h=0,(len(matrix[0])-1)
        while(l<=h):
            m=(l+h)//2
            if(matrix[r][m]<target):
                l=m+1
            elif(matrix[r][m]>target):
                h=m-1
            else:
                return True
        return False
