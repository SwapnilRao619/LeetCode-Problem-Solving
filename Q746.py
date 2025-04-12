## N
## Idea, approach and time complexity:
'''
The solution uses a **top-down dynamic programming (DP)** approach with **memoization** to find the minimum cost to climb the stairs. The main idea is to define a 
recursive function (`helper(i, cache)`) that calculates the minimum cost to reach the i-th step by considering the cost of stepping from either the (i-1)-th or (i-2)-th 
step. The function stores previously computed results in a cache (or memo) to avoid redundant calculations, optimizing the process. The base case checks if `i` is less 
than 2, in which case no cost is needed. The final answer is the minimum cost to reach the top of the stairs, starting from the `n`-th step. The solution visits each 
step at most once, and each recursive call works in constant time due to memoization. Thus, the time complexity is **O(n)**, where `n` is the length of the `cost` array. 
The space complexity is also **O(n)** due to the storage required for the memoization cache.
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        def helper(i,cache):
            if(i in cache):
                return cache[i]
            if(i<2):
                return 0
            val=min(cost[i-1]+helper(i-1,cache),cost[i-2]+helper(i-2,cache))
            cache[i]=val
            return val
        return helper(n,{})