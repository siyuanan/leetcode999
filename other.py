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
