## N
## Idea, approach and time complexity:
'''
The solution determines the type of a triangle based on the side lengths provided in the list `nums`. First, it checks if the given sides satisfy the triangle inequality 
theorem, ensuring that the sum of any two sides is greater than the third. If the sides form a valid triangle, it then classifies the triangle as "equilateral" (all sides 
equal), "isosceles" (two sides equal), or "scalene" (no sides equal). If the sides do not satisfy the triangle inequality, it returns "none". The time complexity is O(1), 
as the solution involves only a constant number of comparisons.
'''

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if(nums[0]+nums[1]>nums[2] and nums[1]+nums[2]>nums[0] and nums[2]+nums[0]>nums[1]):
            if(nums[0]==nums[1] and nums[0]==nums[2]):
                return "equilateral"
            elif(nums[0]==nums[1] or nums[1]==nums[2] or nums[2]==nums[0]):
                return "isosceles"
            else:
                return "scalene"
        return "none"