## N
## Idea, approach and time complexity:
'''
## A1:
The idea behind this solution is to check if two strings are anagrams by comparing their sorted character sequences. The approach involves first checking if the lengths 
of the strings are equal; if not, they cannot be anagrams. If the lengths match, the function sorts both strings and compares the results. The time complexity is 
\(O(n \log n)\), where \(n\) is the length of the strings, due to the sorting operation.

##A2:
The idea behind this solution is to count the frequency of each character in both strings and then compare these counts to determine if they are anagrams. The approach 
uses two dictionaries to store character counts for each string. After populating the dictionaries, it checks if the counts match for all characters in the first string. 
The time complexity is \(O(n)\), where \(n\) is the length of the strings, due to the linear traversal for counting and the comparison of the character counts.
'''

## A1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        return sorted(s)==sorted(t)
    
## A2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        shm,thm={},{}
        for i in range(len(s)):
            shm[s[i]]=1+shm.get(s[i],0)
            thm[t[i]]=1+thm.get(t[i],0)
        for j in shm:
            if shm[j]!=thm.get(j,0):
                return False
        return True