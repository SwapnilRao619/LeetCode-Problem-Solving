## N
## Idea, approach and time complexity:
'''
The problem requires grouping anagrams from a list of strings. The approach involves using a hash map (dictionary) where the keys are the sorted characters of each 
string, and the values are lists of strings that are anagrams of each other. By iterating through the list, each string is sorted to form the key, and the string is 
appended to the corresponding list in the hash map. The time complexity is O(N * K log K), where N is the number of strings and K is the maximum length of a string, due 
to the sorting operation for each string.
'''

class Solution:
    def groupAnagrams(self, strs):
        hm={}
        for i in strs:
            key=''.join(sorted(i))
            if key in hm:
                hm[key].append(i)
            else:
                hm[key]=[i]
        return hm.values()