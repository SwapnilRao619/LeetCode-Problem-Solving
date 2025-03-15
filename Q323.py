## N
## Idea, approach and time complexity:
'''
The solution counts the number of connected components in an undirected graph using Breadth-First Search (BFS). It first constructs an adjacency list from the given 
edges. Then, it iterates through each node, and if the node has not been visited, it initiates a BFS to explore all reachable nodes in that connected component, marking 
them as visited. Each time a BFS is initiated from an unvisited node, the count of connected components is incremented. The algorithm ensures all nodes in a component are 
visited and counted correctly. The time complexity is O(N + E), where N is the number of nodes and E is the number of edges, because each node and edge is processed once 
during BFS traversal.
'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count=0
        seen=set()
        al=defaultdict(list)
        for a,b in edges:
            al[a].append(b)
            al[b].append(a)
        def bfs(i):
            seen.add(i)
            q=deque()
            q.append(i)
            while(q):
                node=q.popleft()
                for nei in al[node]:
                    if(nei in seen):
                        continue
                    q.append(nei)
                    seen.add(nei)
        for i in range(n):
            if(i not in seen):
                count+=1
                bfs(i)
        return count