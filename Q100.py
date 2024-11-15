## N
## Idea, approach and time complexity:
'''
The solution modifies the conventional BFS by appending `None` for missing nodes in the level order traversal, ensuring that structural integrity is maintained. This 
allows the algorithm to account for any differences in tree shape, such as missing children in one tree but not the other. By including `None` for absent nodes, the BFS 
effectively compares both the values and the structure of the trees, not just the presence of nodes. The time complexity is O(N + M), where N and M are the number of 
nodes in trees p and q respectively, as each node is visited once during the BFS traversal.
'''

class Solution:
    def bfs(self,root):
        if(not root):
            return []
        q=deque()
        q.append(root)
        ans=[]
        while(q):
            ls=len(q)
            lv=[]
            for _ in range(ls):
                curr=q.popleft()
                if(curr):
                    lv.append(curr.val)
                    q.append(curr.right)
                    q.append(curr.left)
                else:
                    lv.append(None)
            ans.append(lv)
        return ans
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.bfs(p)==self.bfs(q)