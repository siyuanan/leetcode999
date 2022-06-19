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

  # 
