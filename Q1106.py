## N
## Idea, approach and time complexity:
'''
The `parseBoolExpr` function evaluates a boolean expression in string form by parsing it iteratively. The approach involves scanning for the closing parentheses, then 
finding the corresponding opening parenthesis to extract the operator and its operands. Depending on the operator (`&`, `|`, `!`), it evaluates the enclosed expression 
and replaces it with the result, gradually simplifying the entire expression. This continues until a single boolean value is derived. The time complexity is O(n), where 
n is the length of the input string, since each character is processed a limited number of times during the evaluation.
'''

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        exp=list(expression)
        l,r=0,(len(exp)-1)
        while(l<len(exp)):
            if(exp[l]!=")"):
                l+=1
            else:
                r=l
                while(exp[r]!="("):
                    r-=1
                op=exp[r-1]
                temp=[c for c in exp[r+1:l] if c!=',']
                if(op=="&"):
                    result='t' if all(c=="t" for c in temp) else 'f'
                elif(op=="|"):
                    result='t' if any(c=="t" for c in temp) else 'f'
                elif(op=='!'):
                    result='f' if temp[0]=="t" else "t"
                exp=exp[:r-1]+[result]+exp[l+1:]
                l,r=0,0
        return True if exp[0]=='t' else False