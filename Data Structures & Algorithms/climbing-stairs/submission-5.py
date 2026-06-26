class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0
        if n == 1 or n == 2 or n == 3:
            return n
        
        return (self.climbStairs(n - 2) + self.climbStairs(n - 1))        
        