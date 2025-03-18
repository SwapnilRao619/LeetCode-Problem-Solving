## N
## Idea, approach and time complexity:
'''
The given code solves the problem of finding a redundant connection in an undirected graph using a union-find (disjoint-set) data structure. The approach involves 
iterating through each edge and checking whether the two vertices of the edge are already connected by previous edges. If they are, this edge is redundant, and the 
function returns it. The union-find structure helps efficiently determine whether two vertices belong to the same set (connected components) using the `findP` function to 
find the root (representative) of a set. The `union` function merges two sets by making the root of one set point to the root of the other. The process involves first 
initializing the parent array such that each node is its own parent (indicating each node starts as its own set). When processing each edge, the algorithm performs a 
`find` operation to check if the two vertices are connected, and if they are not, it performs a `union` to combine their sets. The time complexity is nearly constant, 
O(α(n)), where α is the inverse Ackermann function, which grows extremely slowly, making the algorithm almost linear in practice. The space complexity is O(n) due to the 
storage required for the parent array.
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        def union(a,b):
            aP,bP=findP(a),findP(b)
            parent[bP]=aP
        def findP(a):
            while(a!=parent[a]):
                a=parent[a]
            return a
        for e in edges:
            if(findP(e[0])==findP(e[1])):
                return e
            union(e[0],e[1])