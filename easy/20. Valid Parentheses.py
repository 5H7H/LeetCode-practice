class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        pairs ={
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }

        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if char != pairs[stack.pop()]:
                    return False
        if stack == None:
            return True
        else:
            return False    



