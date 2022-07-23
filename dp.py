# dynamic programming

class Solution:
    # 70
    def climbStairs(self, n: int) -> int:
        # go to n-2, then go 2 steps (x1)
        # go to n-1, then go 1 steps (x2)
        # so n = (n-2) + (n-1) => x3
        if n <= 2: 
            return n
        
        x1 = 1 # n = 1
        x2 = 2 # n = 2
        i = 3  # start from n = 3
        while i <= n: 
            x3 = x1 + x2
            i += 1
            x1 = x2
            x2 = x3
        return x3
