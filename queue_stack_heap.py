# queue & stack & heap
class Solution:
    # 227. Basic Calculator II
    def calculate(self, s: str) -> int:
        if len(s) <= 0: 
            return 0

        stack = deque()
        operation = '-' if s[0] == '-' else '+'
        curNumber = 0

        for i in range(len(s)): 
            # print(f'i: {i}')
            # get the current number
            if s[i] >= '0' and s[i] <= '9': 
                curNumber = 10 * curNumber + int(s[i])

            # reach the next operation
            # finish previous operation
            if (s[i] in ['+', '-', '*', '/']) or (i == len(s)-1): 
                # print(f'si: {s[i]}')
                # print(curNumber)
                if operation == '+': 
                    stack.append(curNumber)
                elif operation == '-': 
                    stack.append(-curNumber)
                elif operation == '*': 
                    stack.append(stack.pop() * curNumber)
                else: 
                    stack.append(int(stack.pop() / curNumber))
                operation = s[i]
                curNumber = 0
                i += 1
                # print(stack)
                # print(operation)      

        res = 0
        while len(stack) > 0: 
            res += stack.pop()
        return res
    
    215. Kth Largest Element in an Array
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def swap(lst, i, j): 
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
            
        def percolateDown(lst, i): 
            while i < len(lst) // 2: 
                j1 = i*2+1
                j2 = i*2+2
                if j1 < len(lst) and j2 < len(lst): 
                    if lst[i] > lst[j1]: 
                        if lst[j1] <= lst[j2]: 
                            swap(lst, i, j1)
                            i = j1
                        else: 
                            swap(lst, i, j2)
                            i = j2
                            
                    elif lst[i] > lst[j2]: 
                        if lst[j2] <= lst[j1]: 
                            swap(lst, i, j2)
                            i = j2
                        else: 
                            swap(lst, i, j1)
                            i = j1
                    else: 
                        return
                elif j2 == len(lst): 
                    if lst[i] > lst[j1]: 
                        swap(lst, i, j1)
                        i = j1
                    else: 
                        return
                            
        def percolateUp(lst, i): 
            while i > 0: 
                j = (i-1) // 2
                if lst[j] > lst[i]: 
                    swap(lst, i, j)
                    i = j
                else: 
                    return

                
        # maintain a min heap with k elements
        # new element replace the min(top)
        # then percolate down
        h = nums[:1]
        for n in nums[1:]: 
            # print(h)
            if len(h) < k: 
                h.append(n)
                percolateUp(h, len(h)-1) 
            else: 
                if n > h[0]: 
                    h[0] = n
                    percolateDown(h, 0)
        return h[0]
    
    # 71. Simplify Path
    def simplifyPath(self, path: str) -> str:
        s = []
        for part in path.split('/'): 
            if part == '..': 
                if len(s) > 0: 
                    s.pop()
            elif part == '.' or len(part) <= 0: 
                continue
            else: 
                s.append(part)
        return '/' + '/'.join(s)
    
    
    # 973. K Closest Points to Origin
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # define a comparator
        def closer(p1, p2): 
            return (p1[0]*p1[0] + p1[1]*p1[1]) <= (p2[0]*p2[0] + p2[1]*p2[1])
        
        def swap(q, i, j): 
            tmp = q[i]
            q[i] = q[j]
            q[j] = tmp
        
        # percolat up and down in a max heap
        def percolateUp(q, i): 
            while (i > 0) and (closer(q[(i-1)//2], q[i])): 
                swap(q, i, (i-1)//2)
                i = (i-1)//2
                
        def percolateDown(q, i): 
            while (i < len(q)//2): 
                if i*2+2 >= len(q): 
                    if closer(q[i], q[i*2+1]): 
                        swap(q, i, i*2+1)
                    i = i*2+1

                else: 
                    if (closer(q[i], q[i*2+1]) or closer(q[i], q[i*2+2])): 
                        if closer(q[i*2+1], q[i*2+2]): 
                            swap(q, i, i*2+2)
                            i = i*2+2
                        else: 
                            swap(q, i, i*2+1)
                            i = i*2+1
                    else: 
                        i = len(q)
                    
        res = []
        for p in points: 
            if len(res) < k: 
                res.append(p)
                percolateUp(res, len(res)-1)
            else: 
                if closer(p, res[0]): 
                    res[0] = p
                    percolateDown(res, 0)
                    
        return res
