## N
## Idea, approach and time complexity:
'''
The provided solution aims to find a duplicate number in a list of integers where each integer is in the range from 1 to \( n \). It uses bit manipulation to track which 
numbers have been seen by leveraging bitwise operations. The variable `n` acts as a bitmask, where each bit represents whether a corresponding number has been 
encountered. When a number is encountered for the second time, its corresponding bit in `n` will already be set, indicating a duplicate. The approach runs in O(n) time 
complexity, as it processes the list in a single pass, and uses O(1) space for the bitmask.
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=0
        for i in nums:
            if(n&(1<<i)):
                return i
            n=(n|(1<<i))