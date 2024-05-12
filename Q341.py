## Idea, approach and time complexity:
'''This code implements a nested iterator for a nested list of integers. It initializes a stack to hold the integers in the nested list. The approach is to recursively 
flatten the nested list using a depth-first traversal. It starts with the outermost list and iterates through each element. If the element is an integer, it's added to 
the stack. If it's a nested list, the recursion continues until all integers are extracted and added to the stack. The time complexity of the initialization process is 
O(n), where n is the total number of integers in the nested list. This is because every integer is visited once. The hasNext() operation takes constant time, while the 
next() operation takes O(1) time as it pops the last element from the stack.'''

## Code:
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]): #initializing a stack to store integers
        self.stack=[]
        self.r(nestedList) #recursion 
        self.stack.reverse() #because it will help to directly use pop to get the first element
    
    def next(self) -> int:
        return self.stack.pop()
    
    def hasNext(self) -> bool:
        return len(self.stack)>0
    
    def r(self, nested):
        for i in nested:
            if i.isInteger(): #there is a wrapper [] around the integers
                self.stack.append(i.getInteger()) #thus, we use .getInteger to get the integer from it and isInteger to determine if integer or not
            else:
                self.r(i.getList())