## N
## Idea, approach and time complexity:
'''
The function `getConcatenation` aims to concatenate a list `nums` with itself. It does this by iterating twice over the input list, appending 
each element to a new list `ans`. The approach uses a nested loop where the outer loop runs twice, and the inner loop iterates through `nums`. 
The time complexity of this solution is O(n), where n is the length of the input list, because each element is processed twice. However, the 
implementation can be simplified by using list multiplication, e.g., `ans = nums * 2`.
'''

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(2):
            for i in nums:
                ans.append(i)
        return ans