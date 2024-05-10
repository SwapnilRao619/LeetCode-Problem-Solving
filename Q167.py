## Idea, approach and time complexity:
'''The code aims to find two numbers in the given list whose sum equals the target value. It utilizes a two-pointer approach by initializing pointers at the beginning 
and end of the list. The algorithm iterates through the list, calculating the sum of the numbers pointed by the two pointers. If the current sum is greater than the 
target, the right pointer is decremented; if it's less, the left pointer is incremented. If the sum equals the target, the indices of the two numbers are returned. 
This approach achieves a time complexity of O(n), where n is the number of elements in the list, as it traverses the list only once with two pointers.'''

## Code:
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while(l<r):
            csum=numbers[l]+numbers[r]
            if csum>target:
                r-=1
            elif csum<target:
                l+=1
            else:
                return [l+1,r+1]