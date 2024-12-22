## N
## Idea, approach and time complexity:
'''
The given solution generates all possible subsets of the input list `nums` using bitwise operations. It first sorts the array to handle duplicates effectively, as sorting 
ensures that any duplicate elements are grouped together, allowing the solution to check and skip duplicates more easily. Then, it iterates through all possible subsets 
(from 0 to \(2^n - 1\)) and constructs each subset by checking the corresponding bits. After constructing each subset, the solution checks if it is already in the result 
list to avoid duplicates. Sorting helps maintain the order of elements and ensures that subsets with the same elements but in different orders are not counted multiple 
times. The time complexity of this approach is \(O(2^n \cdot n)\), where \(n\) is the length of the input list, due to generating subsets and checking duplicates.
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        n=len(nums)
        ans=[]
        for i in range(2**n):
            sub=[]
            for j in range(n):
                if(i&(1<<j)):
                    sub.append(nums[j])
            if(sub not in ans):
                ans.append(sub)
        return ans