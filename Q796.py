## N
## Idea, approach and time complexity:
'''
The solution determines if one string, `goal`, can be derived from another string, `s`, through left rotations. It uses a helper function to perform the rotation and 
iterates through all possible rotations of `s`, checking each configuration against `goal`. If a match is found, it returns `True`; otherwise, it returns `False` after 
exhausting all possibilities. The overall time complexity is O(n²), where n is the length of `s`, due to the nested checks for each rotation.
'''

class Solution:
    def rotateleft(self,word):
        return word[1:]+word[0]

    def rotateString(self, s: str, goal: str) -> bool:
        count=1
        temp=s
        if(len(goal)<len(s)):
            return False
        while(count<len(s)):
            temp=self.rotateleft(temp)
            if(all(temp[i]==goal[i] for i in range(len(goal))) or s==goal):
                return True
            else:
                count+=1
        return False