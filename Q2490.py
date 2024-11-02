## N
## Idea, approach and time complexity:
'''
The approach checks if each word in the sentence starts with the same letter that the previous word ends with, forming a circular structure. It splits the sentence into 
words, iterates through them, and compares the first letter of the current word with the last letter of the previous word. The time complexity is \(O(n)\), where \(n\) 
is the number of characters in the sentence, as it processes each character once during the split and iteration.
'''

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sa=sentence.split(" ")
        for i in range(len(sa)):
            if(sa[i][0]==sa[i-1][-1]):
                continue
            else:
                return False
        return True