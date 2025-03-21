## N
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