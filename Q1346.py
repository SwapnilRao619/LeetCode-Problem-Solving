## N
## Idea, approach and time complexity:
'''
The approach involves rotating the string `s` one character at a time and checking if the resulting string matches the target string `goal`. The `rot` function creates 
a rotated version of the string by moving the first character to the end. This process continues until all rotations have been checked or a match is found. The time 
complexity is O(n²), where n is the length of the string, due to n rotations, each taking O(n) time for string comparison.
'''

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hm={}
        for i,v in enumerate(arr):
            hm[v]=i
        for i in range(len(arr)):
            if(arr[i]*2 in hm):
                if(hm[arr[i]*2]!=i):
                    return True
        return False