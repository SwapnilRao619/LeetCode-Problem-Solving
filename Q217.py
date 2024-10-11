## N
## Idea, approach and time complexity:
'''
The solution uses a set to track unique elements in the input list `nums`. It iterates through each number, checking if it already exists in the set; if so, it returns 
`True`, indicating a duplicate. If not, it adds the number to the set. The time complexity is O(n), where n is the number of elements in `nums`, as each lookup and 
insertion in a set is on average O(1).
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm=set()
        for i in nums:
            if i in hm:
                return True
            else:
                hm.add(i)
        return False