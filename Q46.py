## N
## Idea, approach and time complexity:
'''
The provided solution generates all possible permutations of a given list of numbers (`nums`) using a backtracking approach. The function `permute` initializes the 
recursive function `perm`, which explores all permutations by swapping elements of the list in place. It iterates through the list, swapping the current element at index 
`ind` with each subsequent element (including itself), then recursively calls itself with the next index (`ind + 1`). Once the recursion reaches the base case where `ind` 
equals the length of the list (`n`), it appends a copy of the current list (`nums[:]`) to the result list `ans`. After each recursive call, the elements are swapped back 
to their original positions to restore the state for the next iteration, ensuring that all permutations are explored without modification of the input list. The time 
complexity of this solution is O(n!), where `n` is the number of elements in the list. This is because there are `n!` possible permutations of a list of size `n`, and 
each permutation requires a constant amount of work (swapping and adding to the result list). The space complexity is O(n) due to the recursion stack and the space used 
for the result list, where each permutation is stored.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def perm(ind,nums):
            if(ind==n):
                ans.append(nums[:])
                return
            for i in range(ind,n):
                nums[ind],nums[i]=nums[i],nums[ind]
                perm(ind+1,nums)
                nums[ind],nums[i]=nums[i],nums[ind]
        perm(0,nums)
        return ans