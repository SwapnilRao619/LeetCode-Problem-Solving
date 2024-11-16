## N
## Idea, approach and time complexity:
'''
The approach used here leverages a **breadth-first search (BFS)** to perform level-order traversal of both the main tree (`root`) and the subtree (`subRoot`). The 
`isSame` function checks if two trees are identical by comparing their BFS traversals. The `isSubtree` function recursively checks if the subtree exists within the main 
tree by comparing each subtree of the main tree with `subRoot` using the `isSame` method. The time complexity is **O(N * M)**, where **N** is the number of nodes in the 
main tree, and **M** is the number of nodes in the subtree, because for each node in the main tree, a BFS is performed to compare it with the subtree.
'''

class Solution:
    def bfs(self,root):
        if(not root):
            return []
        ans=[]
        q=deque()
        q.append(root)
        while(q):
            ls=len(q)
            lv=[]
            for _ in range(ls):
                curr=q.popleft()
                if(curr):
                    lv.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    lv.append(None)
            ans.append(lv)
        return ans

    def isSame(self,root,subRoot):
        return self.bfs(root)==self.bfs(subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(not root):
            return False
        if(self.isSame(root,subRoot)):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)