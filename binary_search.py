# binary search
class Solution:
  # 707
  def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 0: 
            return -1
        if len(nums) == 1: 
            return int(num[0] == target) - 1
        
    	left = 0
	right = len(nums) - 1
	while left <= right: 
	    mid = (left + right) // 2
    	    If nums[mid] == target: 
	        return mid
	    elif target < num[mid]:
	        right = mid - 1
	    else: 
	        left = mid + 1
	return -1

  # 74
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      # helper function  
      def searchRow(row, target): 
          left = 0
          right = len(row) - 1
          while left <= right: 
              mid = (left + right) // 2
              if row[mid] == target: 
                  return True
              elif target < row[mid]: 
                  right = mid - 1
              else: 
                  left = mid + 1
          return False
          
     if len(matrix) <= 0: 
            return False
        if len(matrix[0]) <= 0: 
            return False
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom: 
            m1 = (top + bottom) // 2
            if matrix[m1][0] == target: 
                return True
            elif matrix[m1][0] > target: 
                bottom = m1 - 1
            else: 
                top = m1 + 1
        return searchRow(matrix[top-1], target)

    # 658
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # if k equals the array length
	if len(arr) == k: 
            return arr

        # binary search to get 2 closest elements
        left = 0
        right = len(arr) - 1
        while left < right - 1: 
            # print(arr[left: right + 1])
            mid = (left + right) // 2
            if arr[mid] == x:
                left = mid
                break
	    # not mid + 1, cuz it may jump over the right range
            elif arr[mid] > x: 
                right = max(left + 1, mid)
            else: 
                left = min(mid, right - 1)
	
	# compare the two values to decide which one is the closest
        if abs(arr[right] - x) < abs(arr[left] - x): 
            left = right
            
        # left will be the index of closest value now
        # expand from left
        right = left
        while right - left + 1 < k: 
            if left == 0: 
                right += 1
            elif right == len(arr) - 1: 
                left -= 1
            elif abs(arr[right + 1] - x) < abs(arr[left - 1] - x):
                right += 1
            else: 
                left -= 1

        return arr[left:right+1]

    # 34
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchFirst(nums, target): 
            if len(nums) == 0: 
                return -1

            left = 0
            right = len(nums) - 1
            while left < right: 
                mid = (left + right) // 2
                if (nums[mid] == target): 
                    if (mid == 0) | (nums[mid-1] != target): 
                        return mid
                if nums[mid] < target: 
                    left = mid + 1
                else: 
                    right = mid - 1

            if nums[left] == target: 
                return left
            else: 
                return -1

        def searchLast(nums, target): 
            if len(nums) == 0: 
                return -1
            left = 0
            right = len(nums) - 1
            while left < right: 
                mid = (left + right) // 2
                if (nums[mid] == target) & (nums[mid+1] != target): 
                    return mid
                if nums[mid] > target: 
                    right = mid - 1
                else: 
                    left = mid + 1

            if nums[left] == target: 
                return left
            else: 
                return -1
            
        i = searchFirst(nums, target)
        if i == -1: 
            return [-1, -1]
        else: 
            return [i, searchLast(nums, target)]

    # 744
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:      
        if target == 'z': 
            return letters[0]
        left = 0
        right = len(letters) - 1
        while left < right: 
            mid = (left + right) // 2
            if letters[mid] > target: 
                if mid == 0: 
                    return letters[mid]
                elif letters[mid-1] <= target: 
                    return letters[mid]
                else: 
                    right = mid - 1
            else: 
                left = mid + 1
            
        if letters[left] <= target:
            return letters[0]
        else: 
            return letters[left]

    # 702
    def search(self, reader: 'ArrayReader', target: int) -> int:
        # find the right boundary
        left = 0
        right = 1
        while reader.get(right) < target:
            right = right * 2
            
        while left <= right:
            mid = (left + right) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return -1
