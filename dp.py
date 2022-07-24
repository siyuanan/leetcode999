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
    
    # 72 min edit distance
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        if m * n == 0:
            return m + n
        
        # dp matrix initialize
        M = [[0] * (m + 1) for x in range(n + 1)]
        for j in range(m + 1): 
            M[0][j] = j
        for i in range(n + 1): 
            M[i][0] = i
            
        # fill dp matrix
        for i in range(1, n+1): 
            for j in range(1, m+1): 
                if word1[j-1] == word2[i-1]: 
                    M[i][j] = 1 + min(M[i-1][j], M[i][j-1], M[i-1][j-1]-1)
                else: 
                    M[i][j] = 1 + min(M[i-1][j], M[i][j-1], M[i-1][j-1])
        
        return M[n][m]
    
