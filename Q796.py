## N
## Idea, approach and time complexity:
'''
The approach involves rotating the string `s` one character at a time and checking if the resulting string matches the target string `goal`. The `rot` function creates 
a rotated version of the string by moving the first character to the end. This process continues until all rotations have been checked or a match is found. The time 
complexity is O(n²), where n is the length of the string, due to n rotations, each taking O(n) time for string comparison.
'''

class Solution:
    def rot(self,word):
        return word[1:]+word[0]

    def rotateString(self, s: str, goal: str) -> bool:
        temp=s
        i=0
        while(i<len(s)):
            temp=self.rot(temp)
            if(temp==goal):
                return True
            else:
                i+=1
        return False
