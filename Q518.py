## N
## Idea, approach and time complexity:
'''
The provided code implements a dynamic programming solution to the **coin change II** problem, where the goal is to find the number of ways to make up a given `amount` 
using an unlimited supply of given coin denominations in the list `coins`. The idea is to use a 2D DP table `t`, where `t[i][j]` represents the number of ways to make up 
amount `j` using the first `i` types of coins. The table is initialized with `t[0][0] = 1` because there is exactly one way to make amount 0 using 0 coins — by choosing 
none. For other cells in the first row, values are 0 since no amount >0 can be formed without using any coin. The core of the approach involves filling in the table by 
considering two cases for each coin: include it (if the coin’s value is less than or equal to the current amount `b`) or exclude it. The final answer is found in 
`t[n][amount]`, where `n` is the number of coin types. This approach ensures all unique combinations are considered without duplication. The **time complexity** is 
**O(n * amount)** and the **space complexity** is also **O(n * amount)** due to the use of a 2D DP table.
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        t=[[0 for _ in range(amount+1)] for _ in range(n+1)]
        t[0][0]=1
        for b in range(1,amount+1):
            t[0][b]=0
        for a in range(1,n+1):
            for b in range(amount+1):
                if(coins[a-1]<=b):
                    t[a][b]=t[a][b-coins[a-1]]+t[a-1][b]
                else:
                    t[a][b]=t[a-1][b]
        return t[n][amount]