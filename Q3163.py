## N
## Idea, approach and time complexity:
'''
The provided solution compresses a string by counting consecutive characters and encoding them as "count followed by character." The approach uses two pointers (`j` and 
`p`) to traverse the string, incrementing a counter `c` for consecutive characters until a different character is found. Once a new character is encountered, it appends 
the count and character to the compressed string. The time complexity of this solution is O(n), where n is the length of the input string, as it processes each character 
exactly once.
'''

class Solution:
    def compressedString(self, word: str) -> str:
        j,p,c=0,0,0
        comp=""
        while(j<len(word)):
            if(word[j]==word[p] and c<9):
                j,c=j+1,c+1
            else:
                comp+=str(c)+word[p]
                c,p=0,j
        comp+=str(c)+word[p]
        return comp