## N
## Idea, approach and time complexity:
'''
The code implements a two-pointer approach to solve the "Two Sum" problem on a sorted list. It initializes two pointers, `l` (left) and `r` (right), and adjusts them 
based on the sum of the values they point to relative to the target. If the sum is greater than the target, it moves the right pointer left; if less, it moves the left 
pointer right, and if equal, it returns the indices (1-based). The time complexity is O(n), where n is the length of the input list, as each element is processed at 
most once.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,(len(numbers)-1)
        for i in range(len(numbers)):
            sum=numbers[l]+numbers[r]
            if(sum>target):
                r-=1
            elif(sum<target):
                l+=1
            else:
                return [l+1,r+1]
