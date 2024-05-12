## Idea, approach and time complexity:
'''This code efficiently checks for nearby duplicates within a specified distance `k` in a list of integers. It iterates through the list, maintaining a dictionary where 
each element encountered is associated with its index. If an element is already in the dictionary and the absolute difference between its current index and the index 
stored in the dictionary is less than or equal to `k`, it returns `True`. If no nearby duplicate is found, it returns `False`. With a time complexity of O(n), where n 
is the length of the list, it offers a swift solution by iterating through the list once and performing constant-time operations for each element.'''

## Code:
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i,v in enumerate(nums):
            if v in d and abs(i-d[v])<=k:
                return True
            else:
                d[v]=i
        return False
