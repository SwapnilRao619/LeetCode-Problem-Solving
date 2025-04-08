## N
## Idea, approach and time complexity:
'''
The problem at hand is a variation of the "Last Stone Weight II" problem, which aims to minimize the weight difference between two groups of stones after repeatedly 
smashing the heaviest stones. The approach used in the solution involves dynamic programming to solve a subset sum problem. First, we calculate the total weight of all 
stones (`S`). Then, using a dynamic programming technique, the `zoksp` function calculates the maximum weight that can be achieved by selecting stones such that their 
sum is less than or equal to half of `S` (i.e., `S//2`). The idea is that if we can get a sum close to half of `S`, the remaining sum would automatically balance out, 
minimizing the weight difference. The DP table `t[a][b]` stores the maximum sum achievable with the first `a` stones and a capacity of `b`. After calculating the optimal 
subset sum, the answer is derived by subtracting twice this optimal sum from the total weight `S`, effectively calculating the minimal weight difference between the two 
groups. The time complexity of the solution is O(n * cap), where `n` is the number of stones, and `cap` is the half of the total sum `S//2`. This is because the dynamic 
programming table has dimensions `(n+1) x (cap+1)`, and for each cell, we either take the current stone or leave it, which results in a linear scan over the table. 
Therefore, the time complexity is proportional to the product of the number of stones and half the total sum of the stones.
'''

class Solution:
    def zoksp(self,arr,cap):
        n=len(arr)
        t=[[0 for _ in range(cap+1)] for _ in range(n+1)]
        for a in range(1,n+1):
            for b in range(1,cap+1):
                if(arr[a-1]<=b):
                    t[a][b]=max(t[a-1][b],arr[a-1]+t[a-1][b-arr[a-1]])
                else:
                    t[a][b]=t[a-1][b]
        return t[n][cap]

    def lastStoneWeightII(self, stones: List[int]) -> int:
        S=0
        for i in range(len(stones)):
            S+=stones[i]
        S1=self.zoksp(stones,S//2)
        return S-(2*S1)