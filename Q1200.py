## N
## Idea, approach and time complexity:
'''
The given solution aims to find all pairs of integers in a list where the absolute difference between the integers is the smallest. The approach begins by sorting the 
input array, as the smallest absolute differences will naturally be between adjacent numbers in a sorted array. First, the algorithm iterates through the sorted array to 
find the minimum absolute difference between consecutive elements. This is stored in a variable `m`. Next, the solution performs another loop to identify all pairs whose 
difference equals `m` and appends them to the result list. The time complexity of the solution is dominated by the sorting step, which takes \(O(n \log n)\), where \(n\) 
is the length of the input array. The two subsequent loops each iterate through the array once, contributing an additional \(O(n)\) time complexity, but this is 
overshadowed by the sorting step. Therefore, the overall time complexity is \(O(n \log n)\). The space complexity is \(O(n)\) due to the storage required for the result 
list and the sorted array.
'''

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        m=1000000000
        arr=sorted(arr)
        for i in range(1,len(arr)):
            z=arr[i]-arr[i-1]
            if(z<m):
                m=z
        ans=[]
        for i in range(1,len(arr)):
            if((arr[i]-arr[i-1])==m):
                ans.append([arr[i-1],arr[i]])
        return ans