## N
## Idea, approach and time complexity:
'''
The code simulates a queue of students trying to grab sandwiches in a specific order. It uses a deque to efficiently handle the queue operations. The main idea is to 
iterate through the students and sandwiches, moving students who don't match the current sandwich to the back of the queue. If all remaining students can't eat the 
current sandwich, the process stops. The time complexity is O(n), where n is the number of students, since each student is processed at most twice.
'''

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q=deque(students)
        c=0
        while q:
            if(q[0]==sandwiches[c]):
                q.popleft()
                c+=1
            else:
                q.append(q.popleft())
                if all(s != sandwiches[c] for s in q):
                    break
        return len(q)