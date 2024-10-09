## N
## Idea, approach and time complexity:
'''
The given solution interleaves two halves of the input list `nums`, where the first half contains the first `n` elements and the second half contains the next `n` 
elements. It uses a loop to append elements from each half into a new list `a`. The time complexity is \(O(n)\) since it processes each element once, where \(n\) is the 
number of elements in one half of `nums`.
'''

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        for i in range(0,n):
            a.append(nums[i])
            a.append(nums[i+n])
        return a