## N
## Idea, approach and time complexity:
'''
The solution uses a breadth-first search (BFS) approach to perform a level-order traversal of the binary tree. It starts by enqueueing the root node and iterates through 
each level by dequeuing nodes, appending their values to the result list, and adding their children to the queue for the next level. This ensures that nodes are processed 
level by level. The time complexity is O(N), where N is the number of nodes in the tree, since each node is processed exactly once. 
'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                lv.append(curr.val)
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            ans.append(lv)
        return ans