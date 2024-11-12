## N
## Idea, approach and time complexity:
'''
The solution performs a level-order traversal (BFS) of the binary tree using a queue. For each level, it captures the rightmost node by appending the last node of that 
level to the result. This is done by iterating through all nodes in the queue and enqueuing their left and right children. The time complexity is O(N), where N is the 
number of nodes, and the space complexity is O(W), where W is the maximum width of the tree, corresponding to the largest number of nodes at any level.
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