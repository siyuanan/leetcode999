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
    
    # 121
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = 10**5
        for i in range(len(prices)): 
            if prices[i] < minPrice: 
                minPrice = prices[i]
            elif prices[i] - minPrice > profit:
                profit = prices[i] - minPrice
        return profit
    
    # 42 trapping water with bars
    def trap(self, height: List[int]) -> int:
        # for each index i, find the max hight from index 0 to i (inclusive)
        m_left = [0] * len(height)
        currentMax = 0
        for i in range(len(height)): 
            if height[i] > currentMax: 
                currentMax = height[i]
            m_left[i] = currentMax
            
        # for each index i, find the max hight from index 0 to i (inclusive)
        m_right = [0] * len(height)
        currentMax = 0
        for i in range(len(height)-1, -1, -1):  
            if height[i] > currentMax: 
                currentMax = height[i]
            m_right[i] = currentMax
        
        ans = 0
        for i in range(len(height)): 
            ans += min(m_left[i], m_right[i]) - height[i]
            
        return ans
    
    # 53 max sub-array
    def maxSubArray(self, nums: List[int]) -> int:
        # M[i] is the current max subarray including i
        M = [0] * len(nums)
        M[0] = nums[0]
        currentLeft = 0
        currentRight = 1
        maxLeft = 0
        maxRight = 1
        currentMax = nums[0]
        
        for i in range(1, len(nums)): 
            if M[i-1] > 0: 
                M[i] = M[i-1] + nums[i]
                currentRight += 1
            else: 
                M[i] = nums[i]
                currentLeft = i
                currentRight = i + 1
            if M[i] > currentMax: 
                maxLeft = currentLeft
                maxRight = currentRight
                currentMax = M[i]
                
#         return [maxLeft, maxRight]
        return currentMax

    # 670. Maximum Swap
    def maximumSwap(self, num: int) -> int:
        if num <= 11: 
            return num
        
        # use dp to find the max digit in the remaining part
        # including the current digit
        s = list(str(num))
        max_remain = [0] * len(s)
        m = 0 # current max
        for i in range(len(s)-1, -1, -1): 
            if int(s[i]) > m: 
                m = int(s[i])
            max_remain[i] = m

        j = 0
        while j < len(s) and int(s[j]) >= max_remain[j]: 
            j += 1
        if j < len(s): # swap j with the max in remaining part
            k = len(s)-1
            while max_remain[k] < max_remain[j]: 
                # find the last digit of the max
                k -= 1
            # swap j and k
            tmp = s[j]
            s[j] = s[k]
            s[k] = tmp
        
        return ''.join(s)
