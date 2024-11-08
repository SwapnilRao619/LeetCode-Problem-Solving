## N
## Idea, approach and time complexity:
'''
The approach involves creating an array with elements `start + 2 * i` for `i` ranging from 0 to `n-1`, and then using the XOR operation on all elements in this array. 
The time complexity is **O(n)** since we iterate through the array elements twice: once for creation and once for the XOR operation.
'''

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans=0
        nums=[start+2*i for i in range(n)]
        for i in nums:
            ans^=i
        return ans