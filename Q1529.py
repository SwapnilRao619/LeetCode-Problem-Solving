## N
## Idea, approach and time complexity:
'''
The solution to the problem revolves around determining the minimum number of flips required to turn a binary string (starting from all zeros) into the target string. 
The key idea is to track whether the current value (starting as 0) matches the value at the corresponding index in the target string. If the current value differs from 
the target, a flip is required, and we increment the flip counter. The variable `f` is used to track the current state (either 0 or 1), and `ans` counts the total number 
of flips. The solution iterates through the target string, checking each character and flipping as needed when the state differs from the target. The approach is 
efficient since it only requires a single pass through the string. Therefore, the time complexity of this solution is **O(n)**, where `n` is the length of the target 
string. The space complexity is **O(1)** because only a constant amount of extra space is used.
'''

class Solution:
    def minFlips(self, target: str) -> int:
        f,ans=0,0
        for i in range(len(target)):
            if(int(target[i])!=f):
                f=not(f)
                ans+=1
        return ans