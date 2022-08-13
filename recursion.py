class Solution:
    # gezhong sort
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1: 
            return nums
        
        # selection sort
        def selectionSort(nums):
            for i in range(len(nums)): 
                m = i
                for j in range(i+1, len(nums)): 
                    if nums[j] < nums[m]: 
                        m = j 

                tmp = nums[i]
                nums[i] = nums[m]
                nums[m] = tmp

            return nums

        # merge sort
        def mergeSort(self, nums): 
            if len(nums) > 1:
                m = len(nums) // 2
                l = nums[:m]
                r = nums[m:]

                mergeSort(self, l)
                mergeSort(self, r)

                i = 0
                j = 0
                idx = 0

                # merge
                while i < len(l) and j < len(r): 
                    if l[i] < r[j]: 
                        nums[idx] = l[i]
                        i += 1
                    else: 
                        nums[idx] = r[j]
                        j += 1
                    idx += 1
                while i < len(l): 
                    nums[idx] = l[i]
                    i += 1
                    idx += 1
                while j < len(r): 
                    nums[idx] = r[j]
                    j += 1
                    idx += 1
            return nums
        return mergeSort(self, nums)
        
