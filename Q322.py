## N1
## Idea, approach and time complexity:
'''
The solution uses a **Breadth-First Search (BFS)** approach to solve the coin change problem, where the goal is to find the minimum number of coins required to make a 
given amount using the available coin denominations. It initializes a queue with a starting state of `(0, 0)`, representing zero coins used and a current value of zero. 
The algorithm explores each possible amount incrementally by adding each coin denomination to the current value, pushing new states into the queue. The `visited` list 
ensures that amounts are not revisited, avoiding redundant calculations. The BFS continues until the target amount is reached, and the number of steps (coins used) is 
returned. If the target amount cannot be formed, the function returns `-1`. The time complexity of this approach is `O(amount * n)`, where `amount` is the target value 
and `n` is the number of coin denominations, as each state could be reached from every coin, and each state is processed once. The space complexity is `O(amount)` due to 
the `visited` list and the queue storing the states.
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if(amount==0):
            return 0
        q=deque()
        q.append((0,0))
        visited=[True]+[False]*amount
        nc=0
        while(q):
            nc,cv=q.popleft()
            nc+=1
            for c in coins:
                nv=cv+c
                if(nv==amount):
                    return nc
                if(nv<amount):
                    if(not visited[nv]):
                        q.append((nc,nv))
                        visited[nv]=True
        return -1

## N2
## Idea, approach and time complexity:
'''
The given solution uses dynamic programming to solve the coin change problem. The idea is to build a table (`t`) where `t[i][j]` represents the minimum number of coins 
needed to make an amount `j` using the first `i` types of coins. Initially, the table is filled with infinity (`float('inf')`), representing impossible solutions. The 
base case is that zero coins are needed to make an amount of zero (`t[0][0] = 0`). The algorithm iterates over each coin type and each possible amount, updating the table 
by either choosing to include the current coin (if it can contribute to the amount) or excluding it. The final result is found at `t[n][amount]`. If it's still infinity, 
the amount cannot be formed, and `-1` is returned. The time complexity is **O(n * amount)**, where `n` is the number of coin types and `amount` is the target amount, 
since the algorithm processes each subproblem in the table exactly once.
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        t=[[float('inf') for _ in range(amount+1)] for _ in range(n+1)]
        t[0][0]=0
        for a in range(1,n+1):
            t[a][0]=0
        for a in range(1,n+1):
            for b in range(1,amount+1):
                if(coins[a-1]<=b):
                    t[a][b]=min(t[a][b-coins[a-1]]+1,t[a-1][b])
                else:
                    t[a][b]=t[a-1][b]
        return t[n][amount] if t[n][amount]!=float('inf') else -1
