## N
## Idea, approach and time complexity:
'''
The approach involves splitting the sentence into words and checking each word to see if it starts with the given `searchWord`. For each word, the `checkPref` function 
compares the prefix of the word with the `searchWord`. If a match is found, the function returns the 1-based index of the word; otherwise, it returns `-1`. The time 
complexity is O(n * m), where `n` is the number of words in the sentence, and `m` is the length of the longest word in the sentence.
'''

class Solution:
    def checkPref(self,sw,w):
        for i in range(len(sw)):
            if(sw[i]!=w[i]):
                return False
        return True

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split(" ")
        for w in range(len(sentence)):
            if(len(sentence[w])>=len(searchWord)):
                if self.checkPref(searchWord,sentence[w]):
                    return w+1
        return -1