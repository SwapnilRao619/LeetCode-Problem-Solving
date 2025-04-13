## N
## Idea, approach and time complexity:
'''
The given code solves the "House Robber" problem using a **top-down dynamic programming (DP)** approach with **memoization**. The idea is to decide, for each house (index 
`i`), whether to rob it or skip it. If we rob the current house, we skip the next one and continue recursively. If we skip it, we simply move to the next house. The 
helper function `helper(i, n, cache)` recursively calculates the maximum amount we can rob starting from house `i` to house `n`, while using a cache (a dictionary) to 
store previously computed results and avoid redundant calculations. This reduces the problem's overlapping subproblems, improving efficiency. The time complexity is 
**O(n)**, where `n` is the length of the input list `nums`. Each house is visited only once due to memoization. The space complexity is also **O(n)** because of the 
cache used to store results for each index.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)-1
        def helper(i,n,cache):
            if(i>n):
                return 0
            if(i in cache):
                return cache[i]
            val=max(nums[i]+helper(i+2,n,cache),helper(i+1,n,cache))
            cache[i]=val
            return val
        return helper(0,n,{})