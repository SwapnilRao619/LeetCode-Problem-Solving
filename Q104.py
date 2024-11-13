## N
## Idea, approach and time complexity:
'''
The solution uses a **Breadth-First Search (BFS)** approach to compute the maximum depth of a binary tree. It starts by initializing a queue with the root node and 
iteratively processes each level of the tree. For each level, it adds all child nodes (left and right) to the queue and increments the depth. This continues until all 
levels are processed. The time complexity is **O(N)**, where N is the number of nodes in the tree, because each node is visited exactly once. The space complexity is 
**O(W)**, where W is the maximum width of the tree, representing the number of nodes at the deepest level.
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth=0
        if(not root):
            return depth
        q=deque()
        q.append(root)
        while(q):
            ls=len(q)
            for i in range(ls):
                curr=q.popleft()
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            depth+=1
        return depth