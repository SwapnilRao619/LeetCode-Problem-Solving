## N
## Idea, approach and time complexity:
'''
The solution implements a Depth-First Search (DFS) to detect cycles and find a valid order of courses. It uses a `status` array to track the state of each course: 
unvisited (0), visiting (1), and visited (2). For each course, DFS explores its prerequisites, and if any course leads to a cycle, it returns an empty list. If no cycles 
are found, the course order is returned. The time complexity is O(V + E), where V is the number of courses (vertices) and E is the number of prerequisites (edges).
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans=[]
        status=[0]*numCourses
        al=defaultdict(list)
        for a,b in prerequisites:
            al[a].append(b)
        def dfs(i):
            state=status[i]
            if(state==1):
                return False
            if(state==2):
                return True
            status[i]=1
            for n in al[i]:
                if(not dfs(n)):
                    return False
            status[i]=2
            ans.append(i)
            return True
        for i in range(numCourses):
            if(not dfs(i)):
                return []
        return ans