## N
## Idea, approach and time complexity:
'''
The given solution generates all unique permutations of a list of numbers, ensuring no duplicates are included. The key idea behind the approach is to use backtracking to 
explore all possible permutations while maintaining uniqueness by skipping duplicate numbers. The input list `nums` is first sorted to help identify and skip duplicates 
easily. A recursive helper function `perm` generates the permutations by swapping elements at the current index with those at subsequent positions. A `used` set is used 
to track elements that have already been swapped at each recursion level, preventing duplicate swaps. The recursion stops when the current index reaches the length of the 
list, at which point the current permutation is added to the result list `ans`. The algorithm explores all permutations but avoids generating duplicate permutations by 
skipping repeated numbers at each step. The time complexity of this solution is \(O(n! \cdot n)\), where \(n\) is the number of elements in the input list. This is 
because, in the worst case, there are \(n!\) unique permutations, and for each permutation, generating a copy of the list takes \(O(n)\) time.
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        n=len(nums)
        ans=[]
        def perm(ind,nums):
            if(ind==n):
                ans.append(nums[:])
                return
            used=set()
            for i in range(ind,n):
                if(nums[i] in used):
                    continue
                used.add(nums[i])
                nums[ind],nums[i]=nums[i],nums[ind]
                perm(ind+1,nums)
                nums[ind],nums[i]=nums[i],nums[ind]
        perm(0,nums)
        return ans