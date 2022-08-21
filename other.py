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
    
    # 680. Valid Palindrome II after remove 1 char
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2: 
            return True
        def checkPalindrome(s, l, r): 
            while l < r: 
                if s[l] != s[r]: 
                    return False
                l += 1
                r -= 1
            return True
        
        l = 0
        r = len(s) - 1
        while l < r: 
            if s[l] != s[r]: 
                return checkPalindrome(s, l+1, r) or checkPalindrome(s, l, r-1)
            l += 1
            r -= 1
        return True

    # 283 move 0s to the end
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: 
            return
        # two pointer, will not maintain the relative order
        # l = 0
        # r = len(nums) - 1
        # # from l to r (inclusive) is the unexplored area
        # # from 0 to l-1 are the non-zeros
        # # from r+1 to end are zeros
        # while l <= r: 
        #     if nums[l] == 0: 
        #         nums[l] = nums[r]
        #         nums[r] = 0
        #         r -= 1
        #     else: 
        #         l += 1
        
        # two pointer go together
        slow = 0
        fast = 0
        while fast < len(nums): 
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
            else: 
                fast += 1
        for i in range(slow, len(nums)): 
            nums[i] = 0
            
    # 75 sort colors, rainbow sort
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: 
            return
        
        p0 = 0
        p1 = 0
        p2 = len(nums) - 1
        # 0 - p0-1: 0
        # p0 - p1-1: 1
        # p1 - p2: TBD
        # p2+1 - end: 2
        while p1 <= p2: 
            if nums[p1] == 0: 
                tmp = nums[p0]
                nums[p0] = nums[p1]
                nums[p1] = tmp
                p0 += 1
                p1 += 1
            elif nums[p1] == 1: 
                p1 += 1
            else: 
                tmp = nums[p2]
                nums[p2] = nums[p1]
                nums[p1] = tmp
                p2 -= 1
        return
    
    # 1249. Minimum Remove to Make Valid Parentheses
    def minRemoveToMakeValid(self, s: str) -> str:
        if '(' not in s and ')' not in s: 
            return s
        pos = set() # set to save the positions to remove
        
        left = 0
        for i in range(len(s)): 
            if s[i] == '(': 
                left += 1
            elif s[i] == ')': 
                left -= 1
            if left < 0: 
                pos.add(i)
                left += 1
        
        right = 0
        for j in range(len(s)-1, -1, -1): 
            if s[j] == ')': 
                right += 1
            elif s[j] == '(': 
                right -= 1
            if right < 0: 
                pos.add(j)
                right += 1
        
        s1 = []
        if len(pos) > 0: 
            for k in range(0, len(s)): 
                if k not in pos: 
                    s1.append(s[k])
        # return pos
        return ''.join(s1)
    
    # 408. Valid Word Abbreviation
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w = 0
        a = 0
        while w < len(word) and a < len(abbr): 
            # use <= 0 here so that when first time seeing 0, return False
            if abbr[a] <= '0' or abbr[a] > '9': 
                if word[w] != abbr[a]: 
                    return False
                w += 1
                a += 1
            else: 
                
                cnt = 0
                while (a < len(abbr)) and (abbr[a] >= '0') and (abbr[a] <= '9'): 
                    cnt = cnt * 10 + int(abbr[a])
                    a += 1
                w += cnt
        return w == len(word) and a == len(abbr)
    
    # 8. String to Integer (atoi)
    def myAtoi(self, s: str) -> int:
        if len(s) <= 0: 
            return 0
        i = 0
        while (i < len(s)) and (s[i] == ' '): 
            i += 1
        if i == len(s): 
            return 0
        if (s[i] not in ['-', '+']) and(s[i] < '0' or s[i] > '9'): 
            return 0

        neg = 0
        cnt = 0
        if s[i] == '-': 
            neg = 1
            i += 1
        elif s[i] == '+': 
            i += 1 
            
        while i < len(s) and s[i] >= '0' and s[i] <= '9': 
            cnt = 10 * cnt + int(s[i])
            i += 1
                
        cnt = cnt * (-1)**neg
        if cnt > 2**31 - 1: 
            cnt = 2**31 - 1
        if cnt < - 2**31: 
            cnt = - 2**31
            
        return cnt
    
    # 1570. Dot Product of Two Sparse Vectors implementation
    class SparseVector:
        def __init__(self, nums: List[int]):
            self.values = {}
            self.len = len(nums)
            for i in range(len(nums)): 
                if nums[i] != 0: 
                    self.values[i] = nums[i]

        # Return the dotProduct of two sparse vectors
        def dotProduct(self, vec: 'SparseVector') -> int:
            s = 0
            for i in range(self.len): 
                if (i in self.values.keys()) and (i in vec.values.keys()): 
                    s += self.values[i] * vec.values[i]
            return s
