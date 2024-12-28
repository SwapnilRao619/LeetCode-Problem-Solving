## N
## Idea, approach and time complexity:
'''
The problem involves finding the XOR sum of all possible subsets of a given list of integers. The solution uses bit manipulation to generate all subsets. For each subset, 
represented by the binary form of integers from 0 to \(2^n - 1\), it computes the XOR of the elements included in that subset. The inner loop checks each bit of the 
inary number to determine if the corresponding element from the list is part of the subset. The XOR result for each subset is accumulated. The time complexity of this 
approach is \(O(n \cdot 2^n)\), where \(n\) is the number of elements in the list, as we iterate through all \(2^n\) subsets and perform \(n\) bit checks for each.
'''

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        fis=0
        n=len(nums)
        for i in range(2**n):
            ins=0
            for j in range(n):
                if(i&(1<<j)):
                    ins^=nums[j]
            fis+=ins
        return fis