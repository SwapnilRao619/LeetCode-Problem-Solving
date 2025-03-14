## N
## Idea, approach and time complexity:
'''
The solution to the problem checks whether a given graph with `n` nodes and a list of `edges` forms a valid tree. A valid tree must satisfy two conditions: it should have 
`n-1` edges and it should be connected (i.e., all nodes should be reachable from any starting node). The approach begins by checking if the number of edges is exactly 
`n-1`, which is a necessary condition for a tree. Then, a breadth-first search (BFS) is used, starting from node `0`. It traverses all the nodes, marking them as visited, 
and explores all adjacent nodes. If during the BFS traversal all nodes are visited, then the graph is connected and we return `True`. If not all nodes are visited, the 
graph is disconnected, so we return `False`. The time complexity of this solution is O(n + e), where `n` is the number of nodes and `e` is the number of edges. This is 
because each node and edge is processed at most once during the BFS traversal.
'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(len(edges)!=n-1):
            return False
        q=deque([0])
        seen=set([0])
        al=defaultdict(list)
        for a,b in edges:
            al[a].append(b)
            al[b].append(a)
        while(q):
            node=q.popleft()
            for nei in al[node]:
                if(nei in seen):
                    continue
                seen.add(nei)
                q.append(nei)
        return len(seen)==n