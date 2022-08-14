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
    
    # quick sort
    def quickSort(nums, l, r): 
        if l > r: 
            return
        idx = partition(nums, l, r)
        quickSort(nums, l, idx - 1)
        quickSort(nums, idx + 1, r)

    def partition(nums, l, r): 
        # choose pivot then swap with last element
        pivot = random.randint(l, r)
        tmp = nums[pivot]
        nums[pivot] = nums[r]
        nums[r] = tmp
        i, j = l, r-1
        while i <= j: 
            if nums[i] < nums[r]: 
                i += 1
            elif nums[j] >= nums[r]: 
                j -= 1
            else: 
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1
        tmp = nums[i]
        nums[i] = nums[r]
        nums[r] = tmp
        return i

#     quickSort(nums, 0, len(nums)-1)
#     return nums
        
