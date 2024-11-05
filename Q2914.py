## N
## Idea, approach and time complexity:
'''
The approach tries to count the minimum number of changes required to make adjacent characters in the string equal. It compares characters at indices `i` and `j`, 
increments the change counter if they are different, and then skips to the next pair of characters by incrementing both `i` and `j` by 2. The time complexity is O(n), 
where `n` is the length of the string, because the loop iterates through the string with a step size of 2.
'''

class Solution:
    def minChanges(self, s: str) -> int:
        i,j=0,1
        count=0
        while(i<j and j<len(s)):
            if(s[i]!=s[j]):
                count+=1
                i,j=i+2,j+2
            else:
                i,j=i+2,j+2
        return count