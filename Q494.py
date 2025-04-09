## N
## Idea, approach and time complexity:
'''
The given solution is for the "Target Sum" problem, where the goal is to find the number of ways to assign '+' and '-' signs to a given list of numbers such that the sum 
of the resulting expression equals a target value. The approach leverages dynamic programming (DP) to efficiently solve the problem. The key idea behind this solution is 
to transform the problem into a subset sum problem. By rearranging the original target equation `sum(P) - sum(N) = target`, where `P` is the set of numbers with '+' signs 
and `N` is the set with '-' signs, it can be rewritten as `sum(P) = (S + target) / 2`, where `S` is the sum of all numbers in the input array. This allows the problem to 
be reduced to finding the number of subsets that sum up to `(S + target) / 2`. The `css` function implements a bottom-up dynamic programming approach to solve this subset 
sum problem. The 2D DP table `t[i][j]` stores the number of ways to achieve a sum `j` using the first `i` numbers. The function initializes the base case and iteratively 
fills the table. If an element is smaller than or equal to the current sum, it considers both including and excluding the element in the subset. Finally, the solution is 
found in `t[n][target]`, where `n` is the number of elements in the array. The time complexity of this approach is `O(n * target)`, where `n` is the number of elements in 
the input array and `target` is the target sum, which is the transformed value `(S - target) / 2`. This is because the dynamic programming table has dimensions 
`(n+1) x (target+1)` and each cell requires constant time to fill. The space complexity is also `O(n * target)` due to the storage of the DP table.
'''

class Solution:
    def css(self,arr,tar):
        n=len(arr)
        t=[[0 for _ in range(tar+1)] for _ in range(n+1)]
        t[0][0]=1
        for b in range(1,tar+1):
            t[0][b]=0
        for a in range(1,n+1):
            for b in range(tar+1):
                if(arr[a-1]<=b):
                    t[a][b]=t[a-1][b-arr[a-1]]+t[a-1][b]
                else:
                    t[a][b]=t[a-1][b]
        return t[n][tar]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S=0
        for i in range(len(nums)):
            S+=nums[i]
        if(abs(target)>S or (S-target)%2!=0):
            return 0
        return self.css(nums,(S-target)//2)