## N
## Idea, approach and time complexity:
'''
The solution checks if a given sentence is a pangram (contains all letters of the English alphabet) by iterating through each character of the sentence and removing it 
from a reference string of the alphabet. If all letters are removed by the end of the loop, it confirms the sentence is a pangram. The time complexity is O(n), where n 
is the length of the sentence, since each character is processed once. However, the repeated string replacement leads to an overall complexity of O(n * m) in the worst 
case, where m is the size of the reference string.
'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ref="abcdefghijklmnopqrstuvwxyz"
        for i in sentence:
            if(i in ref):
                ref=ref.replace(i,"")
        return ref==""