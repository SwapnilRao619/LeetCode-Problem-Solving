## N
## Idea, approach and time complexity:
'''
The solution iterates through the list of employee hours and counts how many employees have met or exceeded the target hours. This is accomplished using a simple loop 
that checks each hour against the target. The time complexity of this approach is \(O(n)\), where \(n\) is the number of employees, as it requires a single pass through 
the list.
'''

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count=0
        for i in hours:
            if(i>=target):
                count+=1
        return count