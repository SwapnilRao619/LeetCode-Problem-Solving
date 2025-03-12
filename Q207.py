## N
## Idea, approach and time complexity:
'''
The solution uses Depth-First Search (DFS) to detect cycles in a directed graph, where nodes represent courses and edges represent prerequisites. The graph is built using 
an adjacency list, where each course points to the courses that must be taken before it. The `status` array keeps track of the state of each course: `0` (unvisited), `1` 
(visiting), and `2` (visited). The DFS function explores each course and its prerequisites recursively. If it encounters a course that is currently being visited 
(`status[i] == 1`), a cycle is detected, and the function returns `False`. If all courses are successfully visited without encountering a cycle, the function returns 
`True`. The algorithm ensures that each course and prerequisite is processed at most once, making it efficient. The time complexity of the solution is O(V + E), where V 
is the number of courses (vertices) and E is the number of prerequisites (edges). This is because each course is processed once and each edge is followed once during DFS 
traversal. The space complexity is O(V + E) due to the adjacency list storage and the `status` array used for tracking course states.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        al=defaultdict(list)
        for a,b in prerequisites:
            al[a].append(b)
        status=[0]*numCourses
        def dfs(i):
            state=status[i]
            if(state==1): return False
            if(state==2): return True
            status[i]=1
            for n in al[i]:
                if(not dfs(n)):
                    return False
            status[i]=2
            return True
        for i in range(numCourses):
            if(not dfs(i)):
                return False
        return True