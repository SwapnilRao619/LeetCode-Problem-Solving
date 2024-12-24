## N
## Idea, approach and time complexity:
'''
The given solution is a recursive backtracking approach to find all unique combinations of numbers in `candidates` that sum up to `target`. It explores each candidate 
starting from the current index and either includes the candidate in the current combination or skips it. The function recursively reduces the target and moves forward 
in the list, backtracking when necessary. The time complexity is exponential, as it explores all possible combinations of the candidates, which can be represented as 
\( O(2^n) \) in the worst case, where `n` is the number of candidates. The space complexity is \( O(k) \), where `k` is the maximum depth of recursion (which is the 
length of the combination).
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(candidates)
        def findPath(si,t,ds):
            if(si==n):
                if(t==0):
                    ans.append(ds.copy())
                return
            if(candidates[si]<=t):
                ds.append(candidates[si])
                findPath(si,t-candidates[si],ds)
                ds.remove(ds[-1])
            findPath(si+1,t,ds)
        findPath(0,target,[])
        return ans