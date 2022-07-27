# other questions

class Solution:
    # 5. Longest Palindromic Substring 
    def longestPalindrome(self, s: str) -> str:
        # expand around the center
        maxLeft = 0
        maxRight = 0
        for i in range(1, len(s)): 
            # case 1: odd lenth, center at i
            currentLeft = i
            currentRight = i
            while ((currentLeft >= 0) & (currentRight < len(s))) and (s[currentLeft] == s[currentRight]): 
                currentLeft -= 1
                currentRight += 1
            if (currentRight - currentLeft - 2) > (maxRight - maxLeft): 
                maxLeft = currentLeft + 1
                maxRight = currentRight - 1
            
            # case 2: even length, center at i-1 and i
            currentLeft = i-1
            currentRight = i
            while ((currentLeft >= 0) & (currentRight < len(s))) and (s[currentLeft] == s[currentRight]): 
                currentLeft -= 1
                currentRight += 1
            if (currentRight - currentLeft - 2) > (maxRight - maxLeft): 
                maxLeft = currentLeft + 1
                maxRight = currentRight - 1
        
        return s[maxLeft:maxRight + 1]
