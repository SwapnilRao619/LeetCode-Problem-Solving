## N
## Idea, approach and time complexity:
'''
The problem is a variation of the classic House Robber problem, where houses are arranged in a circle, meaning the first and last houses cannot both be robbed. The 
approach splits the problem into two linear subproblems: one excluding the last house (rob from index 0 to n-1), and the other excluding the first house (rob from index 
1 to n). A helper function with memoization (top-down DP) is used to calculate the maximum amount that can be robbed in each subproblem, choosing between robbing the 
current house plus skipping one, or skipping the current house. The final answer is the maximum of these two cases. The time complexity is **O(n)**, where *n* is the 
number of houses, due to memoization ensuring each index is processed only once.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)-1
        if(n==0):
            return nums[0]
        def helper(i,n,cache):
            if(i>n):
                return 0
            if(i in cache):
                return cache[i]
            val=max(nums[i]+helper(i+2,n,cache),helper(i+1,n,cache))
            cache[i]=val
            return val
        return max(helper(0,n-1,{}),helper(1,n,{}))