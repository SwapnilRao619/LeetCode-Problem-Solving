## N
## Idea, approach and time complexity:
'''
The code evaluates an expression given in Reverse Polish Notation (RPN) using a stack. It iterates through the tokens, pushing numbers onto the stack and performing 
operations when encountering an operator by popping the required operands from the stack. The time complexity is \(O(n)\), where \(n\) is the number of tokens, and the 
space complexity is \(O(n)\) in the worst case due to the stack.
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hm={'+':(lambda a,b: a+b),
            '/':(lambda a,b: b/a),
            '*':(lambda a,b: a*b),
            '-':(lambda a,b: b-a)}
        stack=[]
        for i in tokens:
            if i in hm:
                n1=stack.pop()
                n2=stack.pop()
                val=hm[i](int(n1),int(n2))
                stack.append(int(val))
            else:
                stack.append(int(i))
        return stack[-1]