## N
## Idea, approach and time complexity:
'''
The given solution solves the "Partition Equal Subset Sum" problem, which asks if an array can be partitioned into two subsets with equal sum. The approach leverages 
dynamic programming (DP) to determine if there exists a subset of the array whose sum is equal to half of the total sum of the array. If the total sum of the array is 
odd, the partition is impossible, and the function returns `False`. If the sum is even, it calls the `subsetSum` method, which uses a DP table `t` where `t[i][j]` 
indicates whether it's possible to achieve a sum of `j` using the first `i` elements of the array. The table is built iteratively, checking at each step if the current 
element can either be included or excluded to form the desired sum. The time complexity of this approach is O(n * tar), where `n` is the number of elements in the input 
array, and `tar` is half of the total sum of the array (`asum // 2`). The space complexity is also O(n * tar) due to the DP table.
'''

class Solution:
    def subsetSum(self,arr,tar):
        n=len(arr)
        t=[[None for _ in range(tar+1)] for _ in range(n+1)]
        t[0][0]=True
        for a in range(1,n+1):
            t[a][0]=True
        for b in range(1,tar+1):
            t[0][b]=False
        for a in range(1,n+1):
            for b in range(1,tar+1):
                if(arr[a-1]<=b):
                    t[a][b]=t[a-1][b-arr[a-1]] or t[a-1][b]
                else:
                    t[a][b]=t[a-1][b]
        return t[n][tar]

    def canPartition(self, nums: List[int]) -> bool:
        asum=0
        for i in range(len(nums)):
            asum+=nums[i]
        if(asum%2==0):
            return self.subsetSum(nums,asum//2)
        return False