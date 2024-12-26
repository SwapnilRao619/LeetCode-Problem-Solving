## N
## Idea, approach and time complexity:
'''
This code solves the minimum operations needed to sort each level of a binary tree. The approach uses level-order traversal (BFS) to process the tree level by level, and 
for each level, it counts the minimum number of swaps needed to sort the values using cycle sort approach. The swap counting works by comparing current array with sorted 
array and swapping elements to their correct positions while maintaining a hashmap to track element positions. The time complexity is O(N * log K) where N is total nodes 
and K is maximum nodes in any level, because for each level we sort the values (log K) and may need to perform swaps proportional to level size.
'''

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        res=0
        def cntr(lv):
            swaps=0
            slv=sorted(lv)
            hm={v:k for k,v in enumerate(lv)}
            for i in range(len(lv)):
                if(lv[i]!=slv[i]):
                    swaps+=1
                    j=hm[slv[i]]
                    lv[i],lv[j]=lv[j],lv[i]
                    hm[lv[i]]=i
                    hm[lv[j]]=j
            return swaps 
        while(q):
            lv=[]
            ls=len(q)
            for _ in range(ls):
                node=q.popleft()
                lv.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            res+=cntr(lv)
        return res