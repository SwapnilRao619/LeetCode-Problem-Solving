## N
## Idea, approach and time complexity:
'''
The given solution aims to clone an undirected graph, where each node has a value and a list of neighbors. The approach uses Depth-First Search (DFS) to traverse the 
graph and create a deep copy of it. The function `dfs` takes a dictionary `v` (for storing already cloned nodes) and a node `n` as input. If the node `n` is already 
cloned (i.e., it exists in `v`), it returns the cloned node. If not, it creates a new `Node` object, adds it to the dictionary `v`, and recursively clones all its 
neighbors by appending the result of `dfs` for each neighbor. The function `cloneGraph` initializes an empty dictionary `vis` and calls `dfs` on the starting node. The 
time complexity of this solution is O(N + E), where N is the number of nodes and E is the number of edges in the graph. This is because each node and edge is visited 
once during the DFS traversal. The space complexity is O(N), due to the storage required for the dictionary `v` to store the cloned nodes and the recursion stack.
'''

class Solution:
    def dfs(self, v, n):
        if(n in v):
            return v[n]
        cn=Node(n.val)
        v[n]=cn
        for i in n.neighbors:
            cn.neighbors.append(self.dfs(v,i))
        return cn

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if(node is None):
            return None
        vis={}
        return self.dfs(vis,node)