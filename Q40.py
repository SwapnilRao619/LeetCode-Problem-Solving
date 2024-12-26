## N
## Idea, approach and time complexity:
'''
The given solution uses a backtracking approach to find all unique combinations of numbers from the `candidates` list that sum up to the `target`. First, the candidates 
are sorted to help avoid duplicate combinations, and then the `findPath` function is recursively called to explore all possible combinations. A condition checks if the 
current candidate exceeds the target, in which case the loop breaks early, ensuring efficiency. Additionally, a check `if(i>ind and candidates[i]==candidates[i-1])` 
ensures that duplicates are avoided by skipping the same number at the same recursive depth. The time complexity is O(2^n) where n is the number of candidates, due to the
recursive exploration of all possible combinations. However, sorting the candidates takes O(n log n) time, so the overall complexity is dominated by the combination 
exploration.
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates=sorted(candidates)
        n=len(candidates)
        ans=[]
        def findPath(ind,t,ds):
            if(t==0):
                ans.append(ds[:])
                return
            for i in range(ind,n):
                if(i>ind and candidates[i]==candidates[i-1]):
                    continue
                if(candidates[i]>t):
                    break
                ds.append(candidates[i])
                findPath(i+1,t-candidates[i],ds)
                ds.remove(ds[-1])
        findPath(0,target,[])
        return ans