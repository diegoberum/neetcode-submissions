class Solution:
    def isPalindrome(self, s: str) -> bool:

        # only alphanumeric chars & case-insensitive
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


            
