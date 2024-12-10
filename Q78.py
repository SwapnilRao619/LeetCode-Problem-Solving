## N
## Idea, approach and time complexity:
'''
The given solution generates all possible subsets of a list `nums` using bit manipulation. For each number from 0 to \( 2^n - 1 \), it interprets the binary 
representation as a mask to select which elements to include in the subset. The outer loop runs \( 2^n \) times, and for each iteration, the inner loop checks each bit 
(corresponding to an element in `nums`). The time complexity is \( O(n \cdot 2^n) \), where \( n \) is the length of the list, since there are \( 2^n \) subsets and for 
each subset, we check all \( n \) elements.
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        for i in range(2**n):
            sub=[]
            for j in range(n):
                if(i&(1<<j)):
                    sub.append(nums[j])
            ans.append(sub)
        return ans