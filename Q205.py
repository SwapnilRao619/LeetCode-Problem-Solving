## Idea, approach and time complexity:
'''The code defines a function isIsomorphic that checks whether two strings, s and t, are isomorphic. The idea is to use two dictionaries, d1 and d2, to map characters 
from s to t and vice versa. As the function iterates through the characters of the strings, it checks if there is a conflicting mapping in either dictionary. If a 
conflict is found, it returns False. If no conflicts are found by the end of the iteration, it returns True. The time complexity of this approach is O(n), where n is 
the length of the strings, since the function processes each character of the strings exactly once.'''

## Code:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        self.d1={}
        self.d2={}
        for i in range(len(s)):
            if (s[i] in self.d1 and self.d1[s[i]]!=t[i]) or (t[i] in self.d2 and self.d2[t[i]]!=s[i]):
                return False
            self.d1[s[i]]=t[i]
            self.d2[t[i]]=s[i]
        return True