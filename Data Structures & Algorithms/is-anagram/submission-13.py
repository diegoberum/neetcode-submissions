class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}

        # base case
        if len(s) != len(t):
            return False

        for c in s:
            if c not in seen_s:
                seen_s[c] = 1
            elif c in seen_s:
                seen_s[c] += 1
        
        for c in t: 
            if c not in seen_t:
                seen_t[c] = 1
            elif c in seen_t:
                seen_t[c] += 1

        return seen_s == seen_t
            


       

    


        
        