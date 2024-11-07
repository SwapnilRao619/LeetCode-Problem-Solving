## N
## Idea, approach and time complexity:
'''
The `TimeMap` class efficiently stores key-value pairs with associated timestamps, allowing for retrieval of the most recent value at or before a given timestamp. The 
`set` method appends the `(value, timestamp)` pair to a list for each key, while the `get` method uses binary search to quickly find the correct value for the given 
timestamp. This approach ensures that value lookups are efficient, with a time complexity of O(log n) for retrieval and O(1) for insertion.
'''

class TimeMap:

    def __init__(self):
        self.hm={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.hm):
            self.hm[key]=[]
        self.hm[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.hm):
            return ""
        res=""
        pairs=self.hm[key]
        l,h=0,(len(pairs)-1)
        while(l<=h):
            m=(l+h)//2
            if(pairs[m][1]<=timestamp):
                res=pairs[m][0]
                l=m+1
            else:
                h=m-1
        return res