## N
## Idea, approach and time complexity:
'''
The solution uses a counting sort approach to sort an array of colors represented by integers (0, 1, 2). It first counts the occurrences of each color in a `bucket` 
list, then reconstructs the original array by filling it based on the counts. The time complexity is O(n), where n is the length of the input array, since it makes a 
single pass to count and another to fill the array.
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        bucket=[0,0,0]
        j=0
        for i in nums:
            bucket[i]+=1
        for i,v in enumerate(bucket):
            for k in range(v):
                nums[j]=i
                j+=1