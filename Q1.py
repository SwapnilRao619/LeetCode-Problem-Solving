## N
## Idea, approach and time complexity:
'''
The given code solves the "Two Sum" problem by using a hash map to store the indices of the elements in the input list. It iterates through the list twice: the first 
pass populates the hash map, and the second checks if the complement (target - current element) exists in the map while ensuring it's not the same index. The time 
complexity is (O(n) due to the linear scans, and the space complexity is also (O(n) for the hash map.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(len(nums)):
            hm[nums[i]]=i
        for i in range(len(nums)):
            y=target-nums[i]
            if(y in hm and hm[y]!=i):
                return [i,hm[y]]
