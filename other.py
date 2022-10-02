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
    
    # 791. Custom Sort String
    def customSortString(self, order: str, s: str) -> str:
        # use dictionary to store s
        s_dict = {}
        for c in s: 
            if c in s_dict: 
                s_dict[c] += 1
            else: 
                s_dict[c] = 1
                
        res = []
        for c in order: 
            if c in s_dict: 
                res.append(c * s_dict[c])
                s_dict.pop(c)
                
        for c in s_dict: 
            res.append(c * s_dict[c])
            
        return ''.join(res)
    
    # 11. Container With Most Water
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1: 
            return 0
        w = 0
        l = 0
        r = len(height) - 1
        while l < r: 
            w = max(w, min(height[l], height[r]) * (r - l))
            if height[l] <= height[r]: 
                l += 1
            else: 
                r -= 1
        return w
    
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
    
    # 921. Minimum Add to Make Parentheses Valid
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) <= 0: 
            return 0
        left = 0
        cnt = 0
        for i in range(len(s)): 
            if s[i] == '(': 
                left += 1
            else: 
                left -= 1
            if left < 0: 
                cnt += 1
                left += 1
        cnt += left
        return cnt
    
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
        
    # 249. Group Shifted Strings
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        table = {}
        # first find the hash key for each word
        # shift the word to start with a
        for w in strings: 
            s = ord(w[0]) - ord('a')
            chars = []
            for c in w: 
                if ord(c) - s < ord('a'): 
                    chars.append(chr(26 - s + ord(c)))
                else: 
                    chars.append(chr(ord(c) - s))
            k = ''.join(chars)
            if k not in table.keys(): 
                table[k] = [w]
            else: 
                table[k].append(w)
        result = []
        for k in table.keys(): 
            result.append(table[k])
        return result
    
    # 65. Valid Number
    def isNumber(self, s: str) -> bool:
        if len(s) <= 0: 
            return False
        
        def digit(c): 
            return (c >= '0' and c <= '9')
        def valid(c):
            return digit(c) or c in ['.', '-', '+']
        
        if len(s) == 1: 
            return digit(s)
        
        i = 0
        dot = 0
        e = 0
        e1 = False # number before e
        e2 = False # number after e
        d = False
        while i < len(s): 
            c = s[i]
            if not valid(c) and c.lower() != 'e': 
                return False
            
            elif digit(c): 
                d = True
                if e == 0: 
                    e1 = True
                if e == 1: 
                    e2 = True
                i += 1
                
            elif c.lower() == 'e': 
                if i == 0 or e == 1: 
                    return False
                e += 1
                i += 1
                
            elif c == '.': 
                if dot == 1 or e == 1: 
                    return False
                else: 
                    dot += 1
                    i += 1
            
            elif c in ['-', '+']: 
                if i != 0 and s[i-1].lower() != 'e': 
                    return False
                i += 1
        if e == 1:
            return e1 and e2
        return d
    
    # 498. Diagonal Traverse
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 0: 
            return []
        if len(mat[0]) == 0: 
            return []
        def valid(i, j, mat): 
            return i >= 0 and i < len(mat) and j >= 0 and j < len(mat[0])
        i = 0
        j = 0
        move = [(-1,1), (1,-1)]
        k = 1
        res = []
        while not (i == len(mat)-1 and j == len(mat[0])-1): 
            while valid(i, j, mat): 
                res.append(mat[i][j])
                if k == 1: 
                    diff = move[0]
                else: 
                    diff = move[1]
                i += diff[0]
                j += diff[1]
            if k == 1:
                if i < 0 and j < len(mat[0]): # upper line
                    i += 1
                else: # upper right corner and right line
                    i += 2
                    j -= 1
            else: 
                if i < len(mat) and j < 0: # left line
                    j += 1
                else: # lower left corner and lower line
                    i -= 1
                    j += 2                 
            k = 1-k
        res.append(mat[len(mat)-1][len(mat[0])-1])
        return res
    
    # 560. Subarray Sum Equals K
    # n^3, fail at 10k
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) <= 0: 
            return 0
        l = len(nums)
        cnt = 0
        while l > 0: 
            i = 0
            for j in range(i+l, len(nums)+1): 
                if sum(nums[j-l:j]) == k: 
                    cnt += 1
            l -= 1
            
        return cnt
    
    # n^2 fail at 20k
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) <= 0: 
            return 0
        cnt = 0
        for i in range(len(nums)): 
            s = 0
            for j in range(i, len(nums)): 
                s += nums[j]
                if s == k: 
                    cnt += 1
        return cnt
    
    # O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) <= 0: 
            return 0
        sum_dict = {0: 1}
        s = 0
        cnt = 0
        
        for n in nums: 
            s += n
            if s-k in sum_dict.keys(): 
                cnt += sum_dict[s-k]
            if s in sum_dict.keys(): 
                sum_dict[s] += 1
            else: 
                sum_dict[s] = 1
        return cnt
    
    # 3. Longest Substring Without Repeating Characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: 
            return len(s)
        slow = 0
        fast = 0
        l = 0
        chars = set()
        while fast < len(s): 
            while s[fast] in chars: 
                chars.remove(s[slow])
                slow += 1
            chars.add(s[fast])
            fast += 1
            l = max(fast - slow, l)
        return l
    
    # 6. Zigzag Conversion
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1: 
            return s

        r = []
        i = 0
        while i < numRows: 
            j = i
            if i == 0 or i == numRows-1: 
                while j < len(s): 
                    r.append(s[j])
                    j += (numRows-1)*2
            else: 
                while j < len(s): 
                    r.append(s[j])
                    if j - 2*i + (numRows-1)*2 < len(s): 
                        r.append(s[j - 2*i + (numRows-1)*2])
                    j += (numRows-1)*2
                
            i += 1
        
        return ''.join(r)
    
    
    # 49. Group Anagrams
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # turn each word into a 26 digit string
        table = {}
        for w in strs: 
            k = [0] * 26
            for c in w: 
                k[ord(c) - ord('a')] += 1
            k_str = '-'.join([str(i) for i in k])
            if k_str in table: 
                table[k_str].append(w)
            else: 
                table[k_str] = [w]
        # print(table)
        return [table[k] for k in table]
    
    
    # 31. Next Permutation
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # scan from the last number to the left
        # find the 1st decreasing number
        if len(nums) <= 1: 
            return nums
        def swap(nums, ii, jj): 
            tmp = nums[ii]
            nums[ii] = nums[jj]
            nums[jj] = tmp
        
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]: 
            i -= 1
            
        # now nums[i] is the number to swap to the right
        if i >= 0: # find the decreasing number
            j = i + 1
            while j < len(nums) and nums[j] > nums[i]: 
                j += 1
            swap(nums, i, j - 1)
        
        # last rearrange i+1 to len-1
        # to non-decreasing array
        i = i + 1
        j = len(nums) - 1
        while i < j: 
            swap(nums, i, j)
            i += 1
            j -= 1
            
    # 56. Merge Intervals
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort
        intervals.sort(key = lambda x: x[0])
        # merge
        res = []
        for i in intervals: 
            if len(res) == 0 or i[0] > res[-1][1]: 
                res.append(i)
            else: 
                j = res.pop()
                res.append([min(j[0], i[0]), max(j[1], i[1])])
        return res
    
    # https://leetcode.com/problems/string-without-aaa-or-bbb/submissions/ NOT SUBMITTED YET
    def strWithout3a3b(self, a: int, b: int) -> str:
        def cut(large, small, c1, c2): 
            # cut large with small
            # how many spot 
            spot = (large - 1) // 2
            if small < spot: 
                print(f'{small} too small')
                return ''
            
            n1 = min(small - spot, spot) # how many c2c2 in spot
            n2 = spot - n1 # how many c2 in remaining spot
            res = (c1*2 + c2*2) * n1 + (c1*2 + c2) * n2 
            res += c1 * (large - 2 * spot)
            # if still c2 available
            if small > spot * 2: 
                res += c2 * (small - spot * 2)
            return res
        
        if a > b: 
            return cut(a, b, 'a', 'b')
        else: 
            return cut(b, a, 'b', 'a')
