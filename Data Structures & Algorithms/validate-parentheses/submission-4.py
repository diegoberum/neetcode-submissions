class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(":")", "[":"]", "{":"}"}
    
        for i in range(len(s)):
            if s[i] in brackets:
                stack.append(s[i])
            
            elif s[i] not in brackets:

                if not stack: 
                    return False
                
                top = stack.pop()
                if brackets[top] != s[i]:
                    return False
        
        if stack: 
            return False

        return True
                    


                


        
            




        